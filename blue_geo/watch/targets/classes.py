import copy
from typing import Dict, Tuple
from abcli import file
from abcli.modules import objects
from abcli.file.load import load_yaml
import geopandas as gpd
from shapely.geometry import Polygon
from blue_geo.logger import logger


class Target:
    def __init__(
        self,
        name: str = "",
        catalog: str = "",
        collection: str = "",
        args: Dict[str, str] = {},
    ) -> None:
        self.name: str = name

        self.catalog = catalog
        self.collection = collection

        self.args = copy.deepcopy(args)

    def __repr__(self) -> str:
        return "{}[{}]: {}/{}: {}".format(
            self.__class__.__name__,
            self.name,
            self.catalog,
            self.collection,
            self.args_as_str(" | "),
        )

    def args_as_str(self, delim: str = " ") -> str:
        return delim.join(
            [f"--{argument} {value}" for argument, value in self.args.items()]
        )

    @classmethod
    def load(cls, object_name: str) -> Tuple[bool, "Target"]:
        success, data = file.load_yaml(
            objects.path_of(
                "target/metadata.yaml",
                object_name,
            )
        )

        return success, cls(
            name=data.get("name", ""),
            catalog=data.get("catalog", ""),
            collection=data.get("collection", ""),
            args=copy.deepcopy(data.get("args", {})),
        )

    def save(self, object_name: str) -> bool:
        if not file.save_yaml(
            objects.path_of(
                "target/metadata.yaml",
                object_name,
                create=True,
            ),
            self.__dict__,
        ):
            return False

        lat = self.args.get("lat", 0)
        lon = self.args.get("lon", 0)
        width = self.args.get("width", 0.1)
        height = self.args.get("height", 0.1)

        half_width = width / 2
        half_height = height / 2

        top_left = (lon - half_width, lat + half_height)
        top_right = (lon + half_width, lat + half_height)
        bottom_right = (lon + half_width, lat - half_height)
        bottom_left = (lon - half_width, lat - half_height)

        polygon = Polygon([top_left, top_right, bottom_right, bottom_left, top_left])

        gdf = gpd.GeoDataFrame([1], geometry=[polygon], crs="EPSG:4326")

        return file.save_geojson(
            objects.path_of("target/shape.geojson", object_name),
            gdf,
            log=True,
        )


class TargetList:
    def __init__(self, filename: str = "") -> None:
        self.targets: Dict[str, Target] = {}

        if filename:
            self.load(filename)

    def load(self, filename: str) -> bool:
        self.targets = {}

        success, targets = load_yaml(filename, civilized=True)

        for target_name, target_info in targets.items():
            self.targets[target_name] = Target(
                name=target_name,
                catalog=target_info["catalog"],
                collection=target_info["collection"],
                args=target_info["args"],
            )

        return success
