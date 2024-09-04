from typing import List
from blueness import module
from abcli.modules.host import shell
from blue_geo import NAME
from blue_geo.catalog.EarthSearch.classes import EarthSearchCatalog
from blue_geo.catalog.generic.generic.stac import STACDatacube
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


class EarthSearchSentinel2L1CDatacube(STACDatacube):
    catalog = EarthSearchCatalog()

    collection = "sentinel-2-l1c"

    name = "sentinel_2_l1c"

    s3_prefix = "s3://sentinel-s2-l1c/tiles"

    def ingest_filename(
        self,
        filename: str,
        overwrite: bool = False,
        verbose: bool = False,
    ) -> bool:
        if super().ingest_filename(filename, overwrite, verbose):
            return True

        # https://registry.opendata.aws/sentinel-2/
        return shell(
            "aws s3 cp --request-payer requester {}/{} {}".format(
                self.s3_prefix,
                filename.replace("_", "/"),
                self.full_filename(filename),
            )
        )

    def list_of_files(
        self,
        scope: DatacubeScope = DatacubeScope("all"),
        verbose: bool = False,
    ) -> List[str]:
        list_of_items = [asset.href for asset in self.metadata["Item"].assets.values()]

        list_of_files: List[str] = []
        quick_found = False
        for item in list_of_items:
            item_filename = item.split(f"{self.s3_prefix}/", 1)[1].replace("/", "_")

            includes, quick_found = scope.includes(
                item_filename, -1, verbose, quick_found
            )
            if includes:
                list_of_files.append(item_filename)

        return list_of_files
