from typing import Tuple
from datetime import datetime, timedelta
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from .enums import Area, Source
from abcli import file
from abcli.modules import objects
from abcli.plugins import metadata
from blue_geo.datacube.generic import GenericDatacube
from blue_geo import env
from blue_geo.logger import logger


class FirmsAreaDatacube(GenericDatacube):
    catalog = "firms-area"

    def __init__(
        self,
        source: Source = Source.default(),
        area: Area = Area.default(),
        date: str = "",
        depth: int = 1,
        log: bool = True,
    ):
        super().__init__()

        self.url_prefix = "https://firms.modaps.eosdis.nasa.gov/api/area"
        self.map_key = env.FIRMS_MAP_KEY

        self.area: Area = area
        self.source: Source = source

        self.depth: int = depth

        self.date: str = (
            date if date else (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
        )

        if log:
            logger.info(self.description)

    @property
    def description(self) -> str:
        return "{}, area:{}, source: {} ({})".format(
            super().description,
            self.area.name.lower(),
            self.source.name,
            self.source.description,
        )

    @property
    def datacube_id(self) -> str:
        return "{}-{}-{}".format(
            super().datacube_id,
            self.area.name.lower(),
            self.source.name,
        )

    def ingest(self, object_name: str) -> Tuple[
        bool,
        gpd.GeoDataFrame,
    ]:
        super().ingest(object_name)

        csv_filename = objects.path_of("firms.csv", object_name, create=True)
        if not file.download(
            self.ingest_url(),
            csv_filename,
        ):
            return False, gpd.GeoDataFrame()

        data = pd.read_csv(csv_filename)
        logger.info(f"loaded {len(data):,} point(s).")

        gdf = gpd.GeoDataFrame(
            data,
            geometry=[
                Point(xy)
                for xy in zip(
                    data.longitude,
                    data.latitude,
                )
            ],
            crs="EPSG:4326",  # WGS84
        )

        if not file.save_geojson(
            objects.path_of("firms.geojson", object_name),
            gdf,
        ):
            return False, gdf

        if not metadata.post_to_object(
            object_name,
            "datacube",
            {
                "id": self.datacube_id,
                "source": self.source.name,
                "area": self.area.name,
                "date": self.date,
                "depth": self.depth,
                "len": len(gdf),
            },
        ):
            return False, gdf

        return True, gdf

    def ingest_url(self, html: bool = False) -> str:
        return "{}/{}/{}/{}/{}/{}/{}".format(
            self.url_prefix,
            "html" if html else "csv",
            self.map_key,
            self.source.name,
            self.area.name.lower(),
            self.depth,  # day_range
            self.date,
        )