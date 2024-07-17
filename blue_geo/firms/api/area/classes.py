from typing import Tuple
from datetime import datetime, timedelta
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from . import NAME
from .enums import Area, Source
from abcli import file
from abcli.modules import objects
from blue_geo import env
from blue_geo.logger import logger


class APIRequest:
    def __init__(
        self,
        source: Source = Source.default(),
        area: Area = Area.default(),
        date: str = "",
        depth: int = 1,
        log: bool = True,
    ):
        self.prefix = "https://firms.modaps.eosdis.nasa.gov"
        self.map_key = env.FIRMS_MAP_KEY

        self.area: Area = area
        self.source: Source = source

        self.depth: int = depth

        self.date: str = (
            date if date else (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
        )

        if log:
            logger.info(self.as_str())

    def as_str(self) -> str:
        return "{}.{}, area:{}, source: {} ({})".format(
            NAME,
            self.__class__.__name__,
            self.area.name.lower(),
            self.source.name,
            self.source.description,
        )

    @property
    def datacube_id(self) -> str:
        return "blue-geo-firms-{}-{}".format(
            self.area.name.lower(),
            self.source.name,
        )

    def ingest(self, object_name: str) -> Tuple[
        bool,
        gpd.GeoDataFrame,
    ]:
        logger.info(
            "{}.{} -> {}".format(
                NAME,
                self.__class__.__name__,
                object_name,
            )
        )

        csv_filename = objects.path_of(
            f"{object_name}.csv",
            object_name,
            create=True,
        )
        if not file.download(
            self.url(),
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

        return (
            file.save_geojson(
                objects.path_of(
                    f"{object_name}.geojson",
                    object_name,
                ),
                gdf,
            ),
            gdf,
        )

    def url(self, html: bool = False) -> str:
        return "{}/api/area/{}/{}/{}/{}/{}/{}".format(
            self.prefix,
            "html" if html else "csv",
            self.map_key,
            self.source.name,
            self.area.name.lower(),
            self.depth,  # day_range
            self.date,
        )
