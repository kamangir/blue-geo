from typing import Any, Tuple, List
import boto3
from blue_geo import env
from blue_geo.catalog.copernicus.classes import CopernicusCatalog
from blue_geo.catalog.generic.generic.stac import STACDatacube
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo.logger import logger


class CopernicusSentinel2Datacube(STACDatacube):
    catalog = CopernicusCatalog()

    collection = "SENTINEL-2"

    name = "sentinel_2"

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

    def ingest_filename(
        self,
        filename: str,
        overwrite: bool = False,
        verbose: bool = False,
    ) -> bool:
        if super().ingest_filename(filename, overwrite, verbose):
            return True

        success, bucket, s3_prefix = self.get_bucket(verbose)
        if not success:
            return success

        item_filename = self.full_filename(filename)

        try:
            bucket.download_file(f"{s3_prefix}/{filename}", item_filename)
        except Exception as e:
            logger.error(e)
            return False

        return True

    def list_of_files(
        self,
        scope: DatacubeScope = DatacubeScope("all"),
        verbose: bool = False,
    ) -> List[str]:
        success, bucket, s3_prefix = self.get_bucket()
        if not success:
            return []

        list_of_items = bucket.objects.filter(Prefix=s3_prefix)

        list_of_files: List[str] = []
        quick_found = False
        for item in list_of_items:
            item_filename = item.key.split(f"{s3_prefix}/", 1)[1]

            includes, quick_found = scope.includes(
                item_filename, item.size, verbose, quick_found
            )
            if includes:
                list_of_files.append(item_filename)

        return list_of_files
