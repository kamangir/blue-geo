from typing import Any, List

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

        logger.info("🪄")
        return True

    def list_of_files(
        self,
        scope: DatacubeScope = DatacubeScope("all"),
        verbose: bool = False,
    ) -> List[str]:
        raw_datacube_id = self.raw_datacube_id()

        return scope.filter(
            {
                (
                    value.href.split(f"{raw_datacube_id}/", 1)[1]
                    if raw_datacube_id in value.href
                    else value.href.split("/")[-1]
                ): -1
                for value in self.metadata["Item"].assets.values()
            },
            verbose=verbose,
        )
