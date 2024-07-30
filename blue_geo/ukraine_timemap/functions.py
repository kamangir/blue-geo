from abcli import file, fullname, string
from datetime import datetime
from collections import Counter
from typing import Tuple
from abcli.modules import objects
import geopandas as gpd
from geojson import Point
from blueness import module
from blue_geo import NAME, VERSION
from blue_geo.logger import logger
import matplotlib.pyplot as plt
from typing import Dict
from typing import Any

API_URL = "https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json"

DESCRIPTION = "Civilian Harm in Ukraine TimeMap"


NAME = module.name(__file__, NAME)


def ingest(
    object_name: str,
    do_save: bool = True,
    do_visualize: bool = True,
    log: bool = True,
) -> Tuple[bool, gpd.GeoDataFrame]:
    logger.info(f"{NAME}.ingest -> {object_name}")
    filename = objects.path_of(
        "ukraine_timemap.json",
        object_name,
        create=True,
    )

    gdf = gpd.GeoDataFrame()
    metadata: Dict[str, Any] = {
        "description": DESCRIPTION,
        "created_by": f"{NAME}-{VERSION}.{fullname()}",
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
            record = {
                "geometry": point,
                "sources": ", ".join(event["sources"]),
                "id": event["id"],
                "description": event["description"],
                "date": event["date"],
                "date_obj": datetime.strptime(event["date"], "%m/%d/%Y").date(),
                "location": event["location"],
                "graphic": event["graphic"],
                "associations": ", ".join(event["associations"]),
                "time": event["time"],
            }
        except Exception as e:
            logger.error(f"ingest failed:\nevent: {event}\nerror: {e}")
            failure_count += 1
            continue

        records.append(record)
    gdf = gpd.GeoDataFrame(records)

    gdf.set_crs(epsg=4326, inplace=True)  # WGS 84

    gdf = gdf.sort_values(by="date_obj", ascending=False)

    logger.info("{:,} event(s) -ingested-> gdf.".format(len(gdf)))
    metadata["ingested_count"] = len(gdf)
    if failure_count:
        logger.error(f"{failure_count:,} event(s) failed to ingest.")
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
                    object_name,
                    f"{NAME}-{VERSION}.{fullname()}",
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
                objects.path_of("ukraine_timemap.png", object_name),
                log=log,
            )

    gdf["date"] = gdf["date_obj"].apply(lambda d: f"{d.year}/{d.month:02}/{d.day:02}")

    gdf = gdf.drop(columns=["date_obj"])

    if do_save and not gdf.empty:
        if not file.save_geojson(
            objects.path_of("ukraine_timemap.geojson", object_name),
            gdf,
            log=log,
        ) or not file.save_yaml(
            objects.path_of("metadata.yaml", object_name),
            metadata,
            log=log,
        ):
            return False, gdf

    return True, gdf
