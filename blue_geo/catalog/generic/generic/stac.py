from typing import Tuple, Any, Dict, List
from datetime import datetime, timedelta
from tqdm import tqdm

from blue_objects.metadata import post_to_object

from blue_geo.catalog.generic.generic.classes import GenericDatacube
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo.catalog.generic.stac.classes import STACCatalog
from blue_geo.logger import logger


class STACDatacube(GenericDatacube):
    collection = "unknown"

    QGIS_template = "unknown-template"

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
            "help": "<2024-07-30/2024-08-09>, more: https://documentation.dataspace.copernicus.eu/APIs/STAC.html#search-items-by-datetime",
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
        "keyword": {
            "default": "",
            "help": "<keyword>",
        },
    }

    def ingest(
        self,
        dryrun: bool = False,
        overwrite: bool = False,
        scope: str = "metadata",
        verbose: bool = True,
    ) -> Tuple[bool, Any]:
        success, output = super().ingest(dryrun, overwrite, scope)
        if not success:
            return success, output

        list_of_files = self.list_of_files(DatacubeScope(scope))
        logger.info(
            "ingesting {} file(s){}...".format(
                len(list_of_files),
                " in dryrun mode " if dryrun else "",
            )
        )

        error_count = 0
        for filename in tqdm(list_of_files):
            if dryrun:
                continue

            if not self.ingest_filename(
                filename,
                overwrite=overwrite,
                verbose=verbose,
            ):
                error_count += 1

        if error_count:
            logger.error(f"{error_count} error(s).")

        return error_count == 0, output

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
        keyword: str = "",
        verbose: bool = False,
    ) -> bool:
        assert isinstance(cls.catalog, STACCatalog)

        logger.info(
            "🔎 {}.query -{}> {}".format(
                cls.__name__,
                f"{keyword}-" if keyword else "",
                object_name,
            )
        )

        success, client = cls.catalog.get_client()
        if not success:
            return success

        search_parameters = {
            "collections": [cls.collection],
            "bbox": bbox,
            "datetime": datetime,
            "sortby": [
                {
                    "field": "properties.datetime",
                    "direction": "desc",
                }
            ],
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
            "datacube-{}-{}-{}".format(
                cls.catalog.name,
                cls.name,
                item.id.replace(".SAFE", "-SAFE"),
            )
            for item in items
        ][::-1]

        if keyword:
            list_of_datacube_ids = [
                datacube_id
                for datacube_id in list_of_datacube_ids
                if keyword in datacube_id
            ]

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

    @property
    def raw(self) -> str:
        return "{} @ {}".format(
            super().raw,
            self.metadata["Item"].to_dict(),
        )

    def update_metadata(self, verbose: bool = False) -> bool:
        assert isinstance(self.catalog, STACCatalog)

        if not super().update_metadata(verbose):
            return False

        success, client = self.catalog.get_client()
        if not success:
            return success

        search_parameters = {
            "ids": [self.raw_datacube_id()],
            "collections": [self.collection],
        }

        if verbose:
            for param, value in search_parameters.items():
                logger.info(f"{param}: {value}")

        search = client.search(**search_parameters)

        items = list(search.item_collection())
        if not items:
            return False
        if len(items) != 1 and verbose:
            logger.waring(
                "{}.update_metadata({}): {} instance(s) found.".format(
                    self.__class__.__name__,
                    self.datacube_id,
                    len(items),
                )
            )
        item = items[0]
        if verbose:
            logger.info(
                "🧊 {}: {} @ {}".format(
                    item.id, item.datetime, ", ".join(list(item.assets.keys()))
                )
            )
        self.metadata["Item"] = item

        self.metadata["files"] = self.list_of_files()

        if verbose:
            logger.info(f'{len(self.metadata["files"])} file(s).')
            for index, filename in enumerate(self.metadata["files"]):
                logger.info(f"#{index+1}: {filename}")

        return True
