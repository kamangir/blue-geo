from typing import Any, List

from blue_geo.catalog.SkyFox.classes import SkyFoxCatalog
from blue_geo.catalog.generic.generic.stac import STACDatacube
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo.logger import logger


class SkyFoxVenusDatacube(STACDatacube):
    catalog = SkyFoxCatalog()

    collection = "venus"  # TODO

    name = "venus"

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
        return []
