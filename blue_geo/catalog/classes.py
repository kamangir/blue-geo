from typing import List, Type

from blue_geo import env
from blue_geo.catalog.generic import (
    GenericCatalog,
    VoidCatalog,
    GenericDatacube,
    VoidDatacube,
)
from blue_geo.catalog.copernicus import CopernicusCatalog, CopernicusSentinel2Datacube
from blue_geo.catalog.EarthSearch import (
    EarthSearchCatalog,
    EarthSearchSentinel2L1CDatacube,
)
from blue_geo.catalog.firms import FirmsCatalog
from blue_geo.catalog.firms.area import FirmsAreaDatacube
from blue_geo.catalog.SkyFox import SkyFoxCatalog
from blue_geo.catalog.SkyFox.Venus import SkyFoxVenusDatacube
from blue_geo.catalog.ukraine_timemap import (
    UkraineTimemapCatalog,
    UkraineTimemapDatacube,
)

list_of_catalog_classes: List[Type[GenericCatalog]] = [
    GenericCatalog,
    CopernicusCatalog,
    EarthSearchCatalog,
    FirmsCatalog,
    SkyFoxCatalog,
    UkraineTimemapCatalog,
]

list_of_catalogs: List[str] = sorted(
    [
        catalog_name
        for catalog_name in [
            catalog_class.name for catalog_class in list_of_catalog_classes
        ]
        if catalog_name not in env.BLUE_GEO_DISABLED_CATALOGS.split(",")
    ]
)

list_of_datacube_classes: List[Type[GenericDatacube]] = [
    GenericDatacube,
    FirmsAreaDatacube,
    UkraineTimemapDatacube,
    CopernicusSentinel2Datacube,
    EarthSearchSentinel2L1CDatacube,
    SkyFoxVenusDatacube,
]
