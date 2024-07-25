from typing import Tuple, List
from blue_geo.catalog.generic import GenericCatalog, VoidCatalog
from blue_geo.catalog.firms import FirmsCatalog
from blue_geo.datacube.generic import GenericDatacube, VoidDatacube
from blue_geo.datacube.firms.area import FirmsAreaDatacube

list_of_catalog_classes: list[GenericCatalog] = [
    GenericCatalog,
    FirmsCatalog,
]

list_of_datacube_classes: List[GenericDatacube] = [
    GenericDatacube,
    FirmsAreaDatacube,
]


def get_datacube(datacube_id: str) -> Tuple[bool, GenericDatacube]:
    for datacube_class in list_of_datacube_classes:
        success, _ = datacube_class.parse_datacube_id(datacube_id)
        if success:
            return True, datacube_class(datacube_id)

    return False, VoidDatacube()


def get_datacube_classes_in_catalog(catalog: GenericCatalog) -> list[GenericDatacube]:
    output: list[GenericDatacube] = []
    for datacube_class in list_of_datacube_classes:
        if isinstance(datacube_class.catalog, catalog.__class__):
            output.append(datacube_class)
    return output
