from typing import Dict, Tuple, List
import copy
import geopandas as gpd
from shapely.geometry import Polygon
from functools import reduce
from tqdm import tqdm

from blue_objects import file, objects

from blue_geo.env import BLUE_GEO_WATCH_TARGET_LIST
from blue_geo.logger import logger


class Target:
    def __init__(
        self,
        name: str = "",
        catalog: str = "",
        collection: str = "",
        params: Dict[str, str] = {},
        query_args: Dict[str, str] = {},
        urls: Dict[str, str] = {},
        versions: Dict[str, str] = {},
    ) -> None:
        self.name: str = name

        self.catalog = catalog
        self.collection = collection

        self.params = copy.deepcopy(params)
        self.query_args = copy.deepcopy(query_args)

        self.urls = copy.deepcopy(urls)

        self.versions = copy.deepcopy(versions)

    @classmethod
    def from_dict(
        cls,
        name: str,
        data: Dict,
    ) -> "Target":
        return cls(
            name=name,
            catalog=data.get("catalog", ""),
            collection=data.get("collection", ""),
            params=copy.deepcopy(data.get("params", {})),
            query_args=copy.deepcopy(data.get("query_args", {})),
            urls=copy.deepcopy(data.get("urls", {})),
            versions=copy.deepcopy(data.get("versions", {})),
        )

    def get_version(
        self,
        version: str,
        is_full_name: bool = False,
    ) -> "Target":
        if is_full_name:
            version = version[len(self.name) + 1 :]

        if version not in self.versions:
            return Target()

        version_updates = self.versions.get(version, {})

        params = copy.deepcopy(self.params)
        params.update(version_updates.get("params", {}))

        query_args = copy.deepcopy(self.query_args)
        query_args.update(version_updates.get("query_args", {}))

        return Target(
            name=f"{self.name}-{version}",
            catalog=self.catalog,
            collection=self.collection,
            params=params,
            query_args=query_args,
            urls=self.urls,
        )

    @property
    def lat_and_lon(self) -> str:
        lat = self.query_args["lat"]
        lon = self.query_args["lon"]

        return '`lat: {:.04f}"{}`, `lon: {:.04f}"{}`.'.format(
            abs(lat),
            "N" if lat > 0 else "S",
            abs(lon),
            "E" if lon > 0 else "W",
        )

    @classmethod
    def load(cls, object_name: str) -> Tuple[bool, "Target"]:
        success, metadata = file.load_yaml(
            objects.path_of(
                "target/metadata.yaml",
                object_name,
            )
        )

        return success, Target.from_dict(
            metadata.get("name", ""),
            metadata,
        )

    @property
    def one_liner(self) -> str:
        return "{}: {} | {}/{} | {} | {}{}".format(
            self.__class__.__name__,
            self.name,
            self.catalog,
            self.collection,
            self.query_args_as_str(" | "),
            " | ".join([f"{param}={value}" for param, value in self.params.items()]),
            (
                " | {} version(s): {}".format(
                    len(self.versions),
                    ",".join(self.versions.keys()),
                )
                if self.versions
                else ""
            ),
        )

    @property
    def polygon(self) -> Polygon:
        lat = self.query_args.get("lat", 0)
        lon = self.query_args.get("lon", 0)
        width = self.params.get("width", 0.1)
        height = self.params.get("height", 0.1)

        half_width = width / 2
        half_height = height / 2

        top_left = (lon - half_width, lat + half_height)
        top_right = (lon + half_width, lat + half_height)
        bottom_right = (lon + half_width, lat - half_height)
        bottom_left = (lon - half_width, lat - half_height)

        return Polygon(
            [
                top_left,
                top_right,
                bottom_right,
                bottom_left,
                top_left,
            ]
        )

    def query_args_as_str(self, delim: str = " ") -> str:
        return delim.join(
            [f"--{argument} {value}" for argument, value in self.query_args.items()]
        )

    def save(self, object_name: str) -> bool:
        logger.info(f"saving target: {self.name} -> {object_name}")

        if not file.save_yaml(
            objects.path_of(
                "target/metadata.yaml",
                object_name,
                create=True,
            ),
            self.__dict__,
        ):
            return False

        gdf = gpd.GeoDataFrame(
            {
                "id": ["1"],
                "description": [self.name],
                "geometry": [self.polygon],
            },
            crs="EPSG:4326",
        )

        return file.save_geojson(
            objects.path_of("target/shape.geojson", object_name),
            gdf,
            log=True,
        )

    def urls_as_str(self) -> List[str]:
        return sorted(
            [
                " - [{}]({}){}".format(
                    title,
                    url.split(",", 1)[0],
                    (
                        ": {}".format(
                            self.lat_and_lon
                            if title == "Google Maps"
                            else url.split(",", 1)[1].strip()
                        )
                        if "," in url or title == "Google Maps"
                        else ""
                    ),
                )
                for title, url in self.urls.items()
            ]
        )


class TargetList:
    object_name = BLUE_GEO_WATCH_TARGET_LIST

    def __init__(
        self,
        load: bool = True,
        download: bool = False,
    ) -> None:
        self.list_of_targets: Dict[str, Target] = {}

        if load:
            assert self.load(download)

    @classmethod
    def filename(cls) -> str:
        return objects.path_of(
            filename="metadata.yaml",
            object_name=cls.object_name,
        )

    def get(
        self,
        target_name: str,
        including_versions: bool = True,
    ) -> Target:
        if not target_name:
            return Target()

        if target_name in self.list_of_targets:
            return self.list_of_targets[target_name]

        if not including_versions:
            return Target()

        for existing_target in self.list_of_targets.values():
            if target_name.startswith(existing_target.name):
                return existing_target.get_version(
                    target_name,
                    is_full_name=True,
                )

        return Target()

    def get_list(
        self,
        catalog_name: str = "",
        collection: str = "",
        including_versions: bool = True,
    ) -> List[str]:
        return sorted(
            reduce(
                lambda x, y: x + y,
                [
                    [target.name]
                    + (
                        [f"{target.name}-{version}" for version in target.versions]
                        if including_versions
                        else []
                    )
                    for target in self.list_of_targets.values()
                    if (target.catalog == catalog_name or not catalog_name)
                    and (target.collection == collection or not collection)
                ],
                [],
            )
        )

    def load(
        self,
        download: bool = False,
    ) -> bool:
        if download:
            if not objects.download(
                object_name=self.object_name,
                filename="metadata.yaml",
            ):
                return False

        _, targets = file.load_yaml(self.filename(), ignore_error=True)

        self.list_of_targets = {
            target_name: Target.from_dict(
                target_name,
                target_data,
            )
            for target_name, target_data in targets.items()
        }

        return True

    def save(self, object_name: str) -> bool:
        list_of_targets = self.get_list(including_versions=True)

        logger.info(f"saving {len(list_of_targets)} target(s): {object_name}")

        gdf = gpd.GeoDataFrame(
            {
                "id": [str(index + 1) for index in range(len(list_of_targets))],
                "description": [
                    self.get(target_name=target_name).name
                    for target_name in list_of_targets
                ],
                "geometry": [
                    self.get(target_name=target_name).polygon
                    for target_name in list_of_targets
                ],
            },
            crs="EPSG:4326",
        )

        return file.save_geojson(
            objects.path_of("target/shape.geojson", object_name),
            gdf,
            log=True,
        )

    def test(self) -> bool:
        list_of_targets = self.get_list(
            including_versions=True,
        )
        logger.info(f"testing {len(list_of_targets)} target(s).")

        for target_name in tqdm(list_of_targets):
            target = self.get(
                target_name,
                including_versions=True,
            )
            if not target.name:
                logger.error(f"bad target: {target_name}")
                return False

            try:
                logger.info(target.one_liner)
            except Exception as e:
                logger.error(f"bad target: {target_name} - {e}")
                return False

        return True
