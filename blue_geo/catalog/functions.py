from typing import Type, Union, List
from blue_geo.catalog.classes import list_of_catalog_classes, list_of_datacube_classes
from blue_geo.catalog.generic import (
    GenericCatalog,
    VoidCatalog,
    GenericDatacube,
    VoidDatacube,
)


def get_catalog_class(catalog_name: str) -> Type[GenericCatalog]:
    for catalog_class in list_of_catalog_classes:
        if catalog_class.name == catalog_name:
            return catalog_class

    return VoidCatalog


def get_catalog(catalog_name: str) -> GenericCatalog:
    return get_catalog_class(catalog_name)()


def get_datacube(datacube_id: str) -> GenericDatacube:
    return get_datacube_class(datacube_id)(datacube_id)


def get_datacube_class(datacube_id: str) -> Type[GenericDatacube]:
    for datacube_class in list_of_datacube_classes:
        success, _ = datacube_class.parse_datacube_id(datacube_id)
        if success:
            return datacube_class

    return VoidDatacube


def get_datacube_class_in_catalog(
    catalog_name: str,
    collection_name: str,
) -> Type[GenericDatacube]:
    catalog_class = get_catalog_class(catalog_name)

    return (
        [
            datacube_class
            for datacube_class in get_list_of_datacube_classes(catalog_class)
            if datacube_class.name == collection_name
        ]
        + [GenericDatacube]
    )[0]


def get_list_of_collections(
    catalog_class: Union[Type[GenericCatalog], str],
) -> List[str]:
    catalog = get_catalog(catalog_class)

    return catalog.get_list_of_collections()


def get_list_of_datacube_classes(
    catalog_class: Union[Type[GenericCatalog], str],
) -> List[Type[GenericDatacube]]:
    if isinstance(catalog_class, str):
        catalog_class = get_catalog_class(catalog_class)

    return [
        datacube_class
        for datacube_class in list_of_datacube_classes
        if datacube_class.catalog.__class__ == catalog_class
    ]
