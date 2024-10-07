from typing import Tuple, List, Dict, Any
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
import geopandas as gpd
from geojson import Point

from blueness import module
from blue_options import string
from blue_objects import file, objects
from blue_objects.metadata import post_to_object

from blue_geo import NAME, env, fullname
from blue_geo.catalog.generic import GenericDatacube
from blue_geo.catalog.ukraine_timemap.classes import UkraineTimemapCatalog
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo.host import signature
from blue_geo.logger import logger

API_URL = "https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json"

DESCRIPTION = "Civilian Harm in Ukraine TimeMap"


NAME = module.name(__file__, NAME)


class UkraineTimemapDatacube(GenericDatacube):
    name = "ukraine_timemap"

    catalog = UkraineTimemapCatalog()

    QGIS_template = env.BLUE_GEO_QGIS_TEMPLATE_UKRAINE_TIMEMAP

    def ingest(
        self,
        dryrun: bool = False,
        overwrite: bool = False,
        do_save: bool = True,
        scope: str = "metadata",
        do_visualize: bool = True,
        log: bool = True,
    ) -> Tuple[bool, gpd.GeoDataFrame]:
        success, _ = super().ingest(dryrun, overwrite, scope)
        if not success:
            return success, gpd.GeoDataFrame()

        filename = objects.path_of(
            "ukraine_timemap.json",
            self.datacube_id,
            create=True,
        )

        gdf = gpd.GeoDataFrame()
        metadata: Dict[str, Any] = {
            "description": DESCRIPTION,
            "created_by": "-".join(signature()),
            "creation_date": string.pretty_date(),
        }

        success = file.download(API_URL, filename)
        if not success:
            return success, gdf

        success, list_of_events = file.load_json(filename)
        if not success:
            return success, gdf
        logger.info("{:,} event(s) ingested from the api.".format(len(list_of_events)))
        metadata["api_count"] = len(list_of_events)

        records = []
        failure_count = 0
        for event in list_of_events:
            try:
                point = Point(
                    (
                        float(event["longitude"]),
                        float(event["latitude"]),
                    )
                )
                record = {"geometry": point}

                for keyword, value in event.items():
                    record[keyword] = (
                        ", ".join(value) if isinstance(value, list) else value
                    )

                record["date_obj"] = datetime.strptime(event["date"], "%Y-%m-%d").date()

            except Exception as e:
                logger.warning(f"ingest failed: {e}: {event}")
                failure_count += 1
                continue

            records.append(record)

        if not records:
            logger.error("no records to ingest.")
            return False, gdf

        gdf = gpd.GeoDataFrame(records)

        gdf.set_crs(epsg=4326, inplace=True)  # WGS 84

        gdf = gdf.sort_values(by="date_obj", ascending=False)

        logger.info("{:,} event(s) -ingested-> gdf.".format(len(gdf)))
        metadata["ingested_count"] = len(gdf)
        if failure_count:
            logger.warning(f"{failure_count:,} event(s) failed to ingest.")
        metadata["failure_count"] = failure_count

        histogram = Counter(list(gdf["date_obj"].values))

        dates = sorted(histogram.keys())
        logger.info(
            "{:,} day(s) of events, starting {}, until {}.".format(
                len(dates),
                min(dates),
                max(dates),
            )
        )
        metadata["range"] = [min(dates), max(dates)]

        if do_visualize:
            values = [histogram[date] for date in dates]

            plt.figure(figsize=(10, 5))
            plt.bar(dates, values, color="blue")
            plt.xlabel(
                " | ".join(
                    [
                        "Date",
                        self.datacube_id,
                        fullname(),
                    ]
                )
            )
            plt.ylabel("# Events / Day")
            plt.title(DESCRIPTION)

            date_count = 20
            if len(dates) > date_count:
                selected_dates = [
                    dates[i] for i in range(0, len(dates), len(dates) // date_count)
                ]
                if dates[-1] not in selected_dates:
                    selected_dates.append(dates[-1])
            else:
                selected_dates = dates
            plt.xticks(selected_dates, rotation=45)

            plt.tight_layout()
            plt.grid(True)

            if do_save:
                file.save_fig(
                    objects.path_of("ukraine_timemap.png", self.datacube_id),
                    log=log,
                )

        gdf["date"] = gdf["date_obj"].apply(
            lambda d: f"{d.year}/{d.month:02}/{d.day:02}"
        )

        gdf = gdf.drop(columns=["date_obj"])

        if do_save and not gdf.empty:
            if not file.save_geojson(
                objects.path_of("ukraine_timemap.geojson", self.datacube_id),
                gdf,
                log=log,
            ) or not file.save_yaml(
                objects.path_of("metadata.yaml", self.datacube_id),
                metadata,
                log=log,
            ):
                return False, gdf

        return True, gdf

    def list_of_files(
        self,
        scope: DatacubeScope = DatacubeScope("all"),
        verbose: bool = False,
    ) -> List[str]:
        return [
            f"ukraine_timemap.{extension}"
            for extension in [
                "geojson",
                "json",
                "png",
            ]
        ]

    @classmethod
    def query(cls, object_name: str) -> bool:
        logger.info(f"🔎 {cls.__name__}.query -> {object_name}")

        datacube = cls(
            "datacube-ukraine_timemap-{}".format(
                string.pretty_date(as_filename=True),
            )
        )

        logger.info(f"🧊 {datacube.description}")

        return post_to_object(
            object_name,
            "datacube_id",
            [datacube.datacube_id],
        )
