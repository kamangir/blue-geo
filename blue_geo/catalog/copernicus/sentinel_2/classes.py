from typing import Any, Tuple, Dict, List
from pystac_client import Client
from blueness import module
from blue_geo import NAME
from abcli.plugins.metadata import post_to_object
from blue_geo.catalog.copernicus.classes import CopernicusCatalog
from blue_geo.catalog.generic.datacube import GenericDatacube
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


class CopernicusSentinel2Datacube(GenericDatacube):
    name = "sentinel_2"
    catalog = CopernicusCatalog()
    QGIS_template = "unknown-template"

    @classmethod
    def parse_datacube_id(cls, datacube_id: str) -> Tuple[
        bool,
        Dict[str, Any],
    ]:
        success, _ = super().parse_datacube_id(datacube_id)
        if not success:
            return False, {}

        # datacube-copernicus-sentinel_1-<item_id>
        segments = datacube_id.split("-")
        if len(segments) < 4:
            return False, {}

        if segments[2] != cls.name:
            return False, {}

        return True, {
            "item_id": datacube_id.split("-", 4)[3],
        }

    @classmethod
    def query(
        cls,
        object_name: str,
        datetime: str,
        bbox: List[float],
        count: int,
        verbose: bool = False,
    ) -> bool:
        logger.info(f"🔎 {cls.__name__}.query -> {object_name}")

        try:
            client = Client.open(cls.catalog.url)
        except Exception as e:
            logger.error(e)
            return False

        search_parameters = {
            "collections": ["SENTINEL-2"],
            "bbox": bbox,
            "datetime": datetime,
        }
        for param, value in search_parameters.items():
            logger.info(f"🔎 {param}: {value}")

        try:
            search = client.search(**search_parameters)
        except Exception as e:
            logger.error(e)
            return False

        items = list(search.item_collection())
        if verbose:
            for item in items:
                logger.info(
                    "🧊 {}: {} @ {}".format(
                        item.id, item.datetime, ", ".join(list(item.assets.keys()))
                    )
                )

        list_of_datacube_ids: List[str] = sorted(
            [
                "datacube-{}-{}-{}".format(
                    cls.catalog.name,
                    cls.name,
                    item.id.replace(".SAFE", "-SAFE"),
                )
                for item in items
            ]
        )
        if count != -1:
            list_of_datacube_ids = list_of_datacube_ids[:count]
        logger.info(f"{len(list_of_datacube_ids)} datacubes(s) found.")
        for index, datacube_id in enumerate(list_of_datacube_ids):
            logger.info(f"🧊 {index+1:02}: {datacube_id}")

        return post_to_object(
            object_name,
            "datacube_id",
            list_of_datacube_ids,
        )
