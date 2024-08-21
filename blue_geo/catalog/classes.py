from typing import List, Type
from blue_geo.catalog.generic import (
    GenericCatalog,
    VoidCatalog,
    GenericDatacube,
    VoidDatacube,
)
from blue_geo.catalog.copernicus import CopernicusCatalog, CopernicusSentinel2Datacube
from blue_geo.catalog.firms import FirmsCatalog
from blue_geo.catalog.firms.area import FirmsAreaDatacube
from blue_geo.catalog.ukraine_timemap import (
    UkraineTimemapCatalog,
    UkraineTimemapDatacube,
)

list_of_catalog_classes: List[Type[GenericCatalog]] = [
    GenericCatalog,
    CopernicusCatalog,
    FirmsCatalog,
    UkraineTimemapCatalog,
]

list_of_catalogs: List[str] = sorted(
    [catalog_class.name for catalog_class in list_of_catalog_classes]
)

list_of_datacube_classes: List[Type[GenericDatacube]] = [
    GenericDatacube,
    FirmsAreaDatacube,
    UkraineTimemapDatacube,
    CopernicusSentinel2Datacube,
]
