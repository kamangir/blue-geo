from typing import Tuple, Dict, Any
from datetime import datetime, timedelta
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from abcli import file
from abcli.modules import objects
from abcli.plugins import metadata
from abcli.plugins.metadata import post_to_object
from blue_geo.catalog.firms import FirmsCatalog
from blue_geo.catalog.generic import GenericDatacube
from blue_geo.catalog.firms.area.enums import Area, Source
from blue_geo import env
from blue_geo.logger import logger


class FirmsAreaDatacube(GenericDatacube):
    name = "area"
    catalog = FirmsCatalog()
    QGIS_template = env.BLUE_GEO_FIRMS_AREA_QGIS_TEMPLATE

    def __init__(
        self,
        datacube_id: str = "",
        source: Source = Source.default(),
        area: Area = Area.default(),
        date: str = "",
        depth: int = 1,
    ):
        super().__init__(datacube_id)

        self.url_prefix = "https://firms.modaps.eosdis.nasa.gov/api/area"
        self.map_key = env.FIRMS_MAP_KEY

        if datacube_id:
            success, args = FirmsAreaDatacube.parse_datacube_id(datacube_id)
            assert success

            area = args["area"]
            source = args["source"]
            depth = args["depth"]
            date = args["date"]

        self.area: Area = area
        self.source: Source = source

        self.depth: int = depth

        self.date: str = (
            date if date else (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
        )

    @property
    def description(self) -> str:
        return "{}, area:{}, source:{} ({})".format(
            super().description,
            self.area.name.lower(),
            self.source.name,
            self.source.description,
        )

    @property
    def datacube_id(self) -> str:
        return "{}-{}-{}-{}-{}-{}".format(
            super().datacube_id,
            "area",
            self.area.name.lower(),
            self.source.name,
            self.date,
            self.depth,
        )

    @classmethod
    def parse_datacube_id(cls, datacube_id: str) -> Tuple[
        bool,
        Dict[str, Any],
    ]:
        success, _ = super().parse_datacube_id(datacube_id)
        if not success:
            return False, {}

        # datacube-firm-area-<area>-<source>-yyyy-mm-dd-depth
        # datacube-firms-area-world-MODIS_NRT-2024-07-20-1
        segments = datacube_id.split("-")
        if len(segments) < 9:
            return False, {}

        if segments[2] != "area":
            return False, {}

        area_str = segments[3]
        if area_str not in Area.values():
            return False, {}

        source_str = segments[4]
        if source_str not in Source.values():
            return False, {}

        date = "{}-{}-{}".format(segments[5], segments[6], segments[7])

        depth_str = segments[8]
        if not depth_str.isdigit():
            return False, {}

        return (
            True,
            {
                "area": Area[area_str.upper()],
                "source": Source[source_str],
                "date": date,
                "depth": int(depth_str),
            },
        )

    def ingest(self, object_name: str) -> Tuple[
        bool,
        gpd.GeoDataFrame,
    ]:
        super().ingest(object_name)

        csv_filename = objects.path_of("firms_area.csv", object_name, create=True)
        if not file.download(
            self.ingest_url(),
            csv_filename,
        ):
            return False, gpd.GeoDataFrame()

        data = pd.read_csv(csv_filename)
        if data.empty:
            return False, gpd.GeoDataFrame()

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
            objects.path_of("firms_area.geojson", object_name),
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

    @staticmethod
    def query(object_name: str, **kwargs) -> bool:
        datacube = FirmsAreaDatacube(**kwargs)

        logger.info(f"🧊 {datacube.description}")

        return post_to_object(
            object_name,
            "datacube_id",
            [datacube.datacube_id],
        )
