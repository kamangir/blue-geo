from typing import List, Type, Union
from blue_geo.catalog.firms import FirmsCatalog
from blue_geo.catalog.generic import (
    GenericCatalog,
    VoidCatalog,
    GenericDatacube,
    VoidDatacube,
)
from blue_geo.catalog.firms.area import FirmsAreaDatacube

list_of_catalog_classes: List[Type[GenericCatalog]] = [
    GenericCatalog,
    FirmsCatalog,
]

list_of_catalogs: List[str] = sorted(
    [catalog_class.name for catalog_class in list_of_catalog_classes]
)

list_of_datacube_classes: List[Type[GenericDatacube]] = [
    GenericDatacube,
    FirmsAreaDatacube,
]


def get_catalog_class(catalog_name: str) -> Type[GenericCatalog]:
    for catalog_class in list_of_catalog_classes:
        if catalog_class.name == catalog_name:
            return catalog_class

    return VoidCatalog


def get_catalog(catalog_name: str) -> GenericCatalog:
    return get_catalog_class(catalog_name)()


def get_collections(
    catalog_class: Union[Type[GenericCatalog], str],
) -> List[Type[GenericDatacube]]:
    if isinstance(catalog_class, str):
        catalog_class = get_catalog_class(catalog_class)

    return [
        datacube_class
        for datacube_class in list_of_datacube_classes
        if datacube_class.catalog.__class__ == catalog_class
    ]


def get_datacube(datacube_id: str) -> GenericDatacube:
    return get_datacube_class(datacube_id)(datacube_id)


def get_datacube_class(datacube_id: str) -> Type[GenericDatacube]:
    for datacube_class in list_of_datacube_classes:
        success, _ = datacube_class.parse_datacube_id(datacube_id)
        if success:
            return datacube_class

    return VoidDatacube
