from typing import Any, Tuple, Dict, List, Union
from datetime import datetime, timedelta
from pystac_client import Client
from blueness import module
from blue_geo import NAME
from abcli.plugins.metadata import post_to_object
from blue_geo.catalog.copernicus.classes import CopernicusCatalog
from blue_geo.catalog.generic.generic.classes import GenericDatacube
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


class CopernicusSentinel2Datacube(GenericDatacube):
    name = "sentinel_2"

    catalog = CopernicusCatalog()

    metadata: Any = {}

    query_args = {
        "bbox": {
            "type": str,
            "default": "",
            "help": "<-122.88,51.73,-122.68,51.93>",
        },
        "datetime": {
            "default": "{}/{}".format(
                (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
                datetime.now().strftime("%Y-%m-%d"),
            ),
            "help": "<2024-07-30/2024-08-09>",
        },
        "lat": {
            "type": float,
            "default": 51.83,
            "help": "<51.83>",
        },
        "lon": {
            "type": float,
            "default": -122.78,
            "help": "<-122.78>",
        },
        "count": {
            "type": int,
            "default": -1,
            "help": "<10>, -1: all",
        },
        "radius": {
            "type": float,
            "default": 0.1,
            "help": "<0.1>",
        },
    }

    QGIS_template = "unknown-template"

    def ingest(self, object_name: str) -> Tuple[bool, Any]:
        success, metadata = super().ingest(object_name)
        if not success:
            return success, metadata

        logger.info("🪄")

        return True, metadata

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
    def connect(cls) -> Tuple[bool, Union[Client, None]]:
        try:
            client = Client.open(cls.catalog.url["api"])
        except Exception as e:
            logger.error(e)
            return False, None

        return True, client

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

        success, client = cls.connect()
        if not success:
            return success

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

    def update_metadata(self, verbose: bool = False) -> bool:
        if not super().update_metadata(verbose):
            return False

        success, client = self.connect()
        if not success:
            return success

        segments = self.datacube_id.replace("-SAFE", ".SAFE").split("-", 3)
        assert len(segments) == 4, self.datacube_id
        search_parameters = {"ids": [segments[3]]}

        if verbose:
            for param in search_parameters:
                logger.info(f"{param}: {search_parameters[param]}")

        search = client.search(**search_parameters)

        items = list(search.item_collection())
        if not items:
            return False
        if len(items) != 1 and verbose:
            logger.waring(
                "{}.update_metadata({}): {} instance(s) found.".format(
                    NAME,
                    self.datacube_id,
                    len(items),
                )
            )
        item = items[0]
        self.metadata["Item"] = item

        if verbose:
            logger.info(
                "🧊 {}: {} @ {}".format(
                    item.id, item.datetime, ", ".join(list(item.assets.keys()))
                )
            )

        return True
