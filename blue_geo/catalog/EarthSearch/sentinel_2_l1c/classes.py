from typing import Any, Dict, List
from blueness import module
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

    def list_of_files(
        self,
        scope: DatacubeScope = DatacubeScope("all"),
        verbose: bool = False,
    ) -> List[str]:
        return [...]
