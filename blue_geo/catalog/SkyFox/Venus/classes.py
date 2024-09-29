from typing import List

from blue_objects import host

from blue_geo.catalog.SkyFox.classes import SkyFoxCatalog
from blue_geo.catalog.generic.generic.stac import STACDatacube
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo.logger import logger


class SkyFoxVenusDatacube(STACDatacube):
    catalog = SkyFoxCatalog()

    collection = "venus-l2a"

    name = "Venus"

    def ingest_filename(
        self,
        filename: str,
        overwrite: bool = False,
        verbose: bool = False,
    ) -> bool:
        if super().ingest_filename(filename, overwrite, verbose):
            return True

        s3_uri = ""
        for item in self.metadata["Item"].assets.values():
            if item.href.endswith(filename):
                s3_uri = item.href
                break

        if not s3_uri:
            logger.info(f"{filename}: file not found.")
            return False

        # https://registry.opendata.aws/venus-l2a-cogs/
        return host.shell(
            "aws s3 cp --no-sign-request {} {}".format(
                s3_uri,
                self.full_filename(filename),
            )
        )

    def list_of_files(
        self,
        scope: DatacubeScope = DatacubeScope("all"),
        verbose: bool = False,
    ) -> List[str]:
        raw_datacube_id = self.raw_datacube_id()

        return scope.filter(
            {
                (value.href.split(f"{raw_datacube_id}/", 1)[1]): -1
                for value in self.metadata["Item"].assets.values()
                if raw_datacube_id in value.href
            },
            verbose=verbose,
        )
