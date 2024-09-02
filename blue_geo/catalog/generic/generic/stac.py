import os
from typing import Tuple, Union, Any, Dict, List
from datetime import datetime, timedelta
from tqdm import tqdm
from pystac_client import Client
from abcli import file, path, string
from abcli.modules import objects
from abcli.plugins.metadata import post_to_object
from blue_geo.catalog.generic.generic.classes import GenericDatacube
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

    @classmethod
    def get_client(cls) -> Tuple[bool, Union[Client, None]]:
        try:
            client = Client.open(cls.catalog.url["api"])
        except Exception as e:
            logger.error(e)
            return False, None

        return True, client

    def ingest(
        self,
        dryrun: bool = False,
        overwrite: bool = False,
        what: str = "metadata",
        verbose: bool = False,
    ) -> Tuple[bool, Any]:
        success, output = super().ingest(dryrun, overwrite, what)
        if not success:
            return success, output

        download_all = what == "all"
        download_quick = what == "quick"
        suffix = "" if download_all or download_quick or what == "metadata" else what

        success, bucket, s3_prefix = self.get_bucket(verbose=True)
        if not success:
            return success, output

        datacube_path = objects.object_path(self.datacube_id)
        if not path.create(datacube_path):
            return False, output

        error_count = 0
        TCI_downloaded = False
        list_of_items = bucket.objects.filter(Prefix=s3_prefix)
        for item in tqdm(list_of_items):
            item_suffix = item.key.split(f"{s3_prefix}/", 1)[1]
            if not item_suffix:
                continue

            item_filename = os.path.join(datacube_path, item_suffix)
            if not path.create(file.path(item_filename)):
                error_count += 1
                continue
            if item_filename.endswith(os.sep):
                continue

            skip = True
            if download_all:
                skip = False
            elif item.size <= 10**6 and not any(
                item_filename.endswith(suffix)
                for suffix in [
                    ".jp2",
                    ".tif",
                    ".tiff",
                ]
            ):
                skip = False
            elif (
                download_quick
                and not TCI_downloaded
                and item_filename.endswith(".jp2")
                and "TCI" in item_filename
            ):
                TCI_downloaded = True
                skip = False
            elif suffix and item_filename.endswith(suffix):
                skip = False

            if skip:
                if verbose:
                    logger.info(
                        "skipped {}: {}".format(
                            string.pretty_bytes(item.size),
                            item_suffix,
                        )
                    )
                continue

            if not overwrite and file.exist(item_filename):
                logger.info(f"✅ {item_filename}")
                continue

            logger.info(
                "downloading {}: {} -> {}".format(
                    string.pretty_bytes(item.size),
                    item_suffix,
                    item_filename,
                )
            )
            if dryrun:
                continue

            try:
                bucket.download_file(item.key, item_filename)
            except Exception as e:
                logger.error(e)
                error_count += 1
                continue

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
        logger.info(
            "🔎 {}.query -{}> {}".format(
                cls.__name__,
                f"{keyword}-" if keyword else "",
                object_name,
            )
        )

        success, client = cls.get_client()
        if not success:
            return success

        search_parameters = {
            "collections": [cls.collection],
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

    def update_metadata(self, verbose: bool = False) -> bool:
        if not super().update_metadata(verbose):
            return False

        success, client = self.get_client()
        if not success:
            return success

        segments = self.datacube_id.replace("-SAFE", ".SAFE").split("-", 3)
        assert len(segments) == 4, self.datacube_id
        search_parameters = {"ids": [segments[3]]}

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
