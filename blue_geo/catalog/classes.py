from typing import List, Type
from .firms import FirmsCatalog
from .generic import GenericCatalog, GenericDatacube, VoidDatacube
from .firms.area import FirmsAreaDatacube

list_of_catalog_classes: List[Type[GenericCatalog]] = [
    GenericCatalog,
    FirmsCatalog,
]

list_of_datacube_classes: List[Type[GenericDatacube]] = [
    GenericDatacube,
    FirmsAreaDatacube,
]


def get_datacube(datacube_id: str) -> GenericDatacube:
    return get_datacube_class(datacube_id)(datacube_id)


def get_datacube_class(datacube_id: str) -> Type[GenericDatacube]:
    for datacube_class in list_of_datacube_classes:
        success, _ = datacube_class.parse_datacube_id(datacube_id)
        if success:
            return datacube_class

    return VoidDatacube


def get_datacube_classes(
    catalog_class: Type[GenericCatalog],
) -> List[Type[GenericDatacube]]:
    return [
        datacube_class
        for datacube_class in list_of_datacube_classes
        if isinstance(datacube_class.catalog, catalog_class)
    ]