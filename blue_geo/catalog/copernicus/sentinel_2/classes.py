import os
from typing import Any, Tuple, Dict, List, Union
import boto3
from datetime import datetime, timedelta
from pystac_client import Client
from tqdm import tqdm
from blueness import module
from abcli import file, path, string
from abcli.modules import objects
from blue_geo import NAME
from blue_geo import env
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

    def get_bucket(self, verbose: bool = False) -> Tuple[bool, Any, str]:
        try:
            href = (
                self.metadata["Item"]
                .assets["PRODUCT"]
                .extra_fields.get("alternate")["s3"]["href"]
            )
        except:
            return False, None, ""

        bucket_name, s3_prefix = href.split("/", 2)[1:3]

        if verbose:
            logger.info(f"href: {href}")
            logger.info(f"bucket_name: {bucket_name}")
            logger.info(f"s3_prefix: {s3_prefix}")

        s3 = boto3.resource(
            "s3",
            endpoint_url="https://eodata.dataspace.copernicus.eu",
            aws_access_key_id=env.COPERNICUS_AWS_ACCESS_KEY_ID,
            aws_secret_access_key=env.COPERNICUS_AWS_SECRET_ACCESS_KEY,
            region_name="default",
        )

        bucket = s3.Bucket(bucket_name)

        return True, bucket, s3_prefix

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

        list_of_items = bucket.objects.filter(Prefix=s3_prefix)

        error_count = 0
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

            if not overwrite and file.exist(item_filename):
                logger.info(f"✅ {item_filename}")
                continue

            if (
                not item.size <= 10**6
                and not download_all
                and not (download_quick and item_filename.endswith("TCI.jp2"))
                and not (suffix and item_filename.endswith(suffix))
            ):
                logger.info(
                    "skipped {}: {}".format(
                        string.pretty_bytes(item.size),
                        item.key,
                    )
                )
                continue

            logger.info(
                "downloading {}: {} -> {}".format(
                    string.pretty_bytes(item.size),
                    item.key,
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
        verbose: bool = False,
    ) -> bool:
        logger.info(f"🔎 {cls.__name__}.query -> {object_name}")

        success, client = cls.get_client()
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
                    NAME,
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

        success, bucket, s3_prefix = self.get_bucket(verbose)

        list_of_files = [
            item.key.split(f"{s3_prefix}/", 1)[1]
            for item in bucket.objects.filter(Prefix=s3_prefix)
        ]
        self.metadata["files"] = list_of_files

        if verbose:
            logger.info(f"{len(list_of_files)} file(s).")
            for index, filename in enumerate(list_of_files):
                logger.info(f"#{index+1}: {filename}")

        return True
