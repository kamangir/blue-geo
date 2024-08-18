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
    def query(
        cls,
        object_name: str,
        datetime: str,
        bbox: List[float],
        limit: int = 16,
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
            "limit": limit,
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

        list_of_datacube_ids: List[str] = [
            item.id.replace(".SAFE", "-SAFE") for item in items
        ]
        logger.info(f"{len(list_of_datacube_ids)} datacubes(s) found.")
        for index, datacube_id in enumerate(list_of_datacube_ids):
            logger.info(f"🧊 {index+1:02}: {datacube_id}")

        return post_to_object(
            object_name,
            "datacube_id",
            list_of_datacube_ids,
        )
