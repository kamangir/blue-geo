from typing import Dict, Tuple, List
import copy
import geopandas as gpd
from shapely.geometry import Polygon

from blue_objects import file, objects

from blue_geo.logger import logger


class Target:
    def __init__(
        self,
        name: str = "",
        description: str = "",
        catalog: str = "",
        collection: str = "",
        params: Dict[str, str] = {},
        query_args: Dict[str, str] = {},
        urls: Dict[str, str] = {},
        versions: Dict[str, str] = {},
    ) -> None:
        self.name: str = name
        self.description: str = description

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
        description = data.get("description", "")
        if not description:
            candidate_description = [
                url.split(",", 1)[1]
                for url in data.get("urls", {}).values()
                if "," in url
            ]
            if candidate_description:
                description = candidate_description[0].strip()

        return cls(
            name=name,
            description=description,
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
            description=self.description,
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
        return "{}: {}{} | {}/{} | {} | {}{}".format(
            self.__class__.__name__,
            self.name,
            " - {}".format(self.description) if self.description else "",
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
                "name": [self.name],
                "description": [self.description],
                "catalog": [self.catalog],
                "collection": [self.collection],
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
