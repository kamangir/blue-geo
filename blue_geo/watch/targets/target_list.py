from typing import Dict, List
import geopandas as gpd
from functools import reduce
from tqdm import tqdm

from blue_objects import file, objects

from blue_geo.env import BLUE_GEO_WATCH_TARGET_LIST
from blue_geo.watch.targets.target import Target
from blue_geo.logger import logger


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

    def download(self) -> bool:
        return objects.download(
            object_name=self.object_name,
            filename="metadata.yaml",
        )

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
        if download and not self.download():
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
                "name": [
                    self.get(target_name=target_name).name
                    for target_name in list_of_targets
                ],
                "description": [
                    self.get(target_name=target_name).description
                    for target_name in list_of_targets
                ],
                "catalog": [
                    self.get(target_name=target_name).catalog
                    for target_name in list_of_targets
                ],
                "collection": [
                    self.get(target_name=target_name).collection
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
