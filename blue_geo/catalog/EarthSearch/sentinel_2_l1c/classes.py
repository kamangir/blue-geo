from typing import List

from blueness import module
from blue_objects import host

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
        verbose: bool = True,
    ) -> bool:
        if super().ingest_filename(filename, overwrite, verbose):
            return True

        # https://registry.opendata.aws/sentinel-2/
        return host.shell(
            "aws s3 cp --request-payer requester {}/{} {}".format(
                self.s3_prefix,
                filename.replace("_", "/"),
                self.full_filename(filename),
            ),
            log=verbose,
        )

    def list_of_files(
        self,
        scope: DatacubeScope = DatacubeScope("all"),
        verbose: bool = False,
    ) -> List[str]:
        return scope.filter(
            [
                {
                    "filename": asset.href.split(f"{self.s3_prefix}/", 1)[1].replace(
                        "/", "_"
                    ),
                }
                for asset in self.metadata["Item"].assets.values()
                if self.s3_prefix in asset.href
            ],
            needed_for_rgb=lambda filename: filename.endswith("TCI.jp2"),
            is_rgb=lambda filename: filename.endswith("TCI.jp2"),
            verbose=verbose,
        )

    @property
    def raw(self) -> str:
        return "{} | {}".format(
            super().raw,
            self.s3_prefix,
        )
