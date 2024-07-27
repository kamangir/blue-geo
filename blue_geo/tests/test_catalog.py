import pytest
from typing import Type
from abcli.modules.objects import unique_object
from blue_geo.tests import assets
from blue_geo.catalog import (
    list_of_catalog_classes,
    list_of_datacube_classes,
    get_datacube,
    get_datacube_class,
    get_datacube_classes,
)
from blue_geo.catalog.generic import GenericCatalog, GenericDatacube


@pytest.mark.parametrize(
    ["catalog_class"],
    [[catalog_class] for catalog_class in list_of_catalog_classes],
)
def test_list_of_catalog_classes(catalog_class: Type[GenericCatalog]):
    catalog = catalog_class()
    assert catalog.name


@pytest.mark.parametrize(
    ["datacube_id", "datacube_class"],
    [
        [datacube_id, datacube_class]
        for datacube_id, datacube_class in assets.datacubes.items()
        if datacube_class in list_of_datacube_classes
    ],
)
def test_list_of_datacube_classes(
    datacube_id: str,
    datacube_class: Type[GenericDatacube],
):
    object_name = unique_object()

    datacube = datacube_class(datacube_id)

    assert datacube.datacube_id

    assert datacube.description

    success, _ = datacube.ingest(object_name)
    assert success


@pytest.mark.parametrize(
    ["datacube_id", "expected_datacube_class"],
    [
        [datacube_id, datacube_class]
        for datacube_id, datacube_class in assets.datacubes.items()
    ],
)
def test_get_datacube(
    datacube_id: str,
    expected_datacube_class: Type[GenericDatacube],
):
    datacube = get_datacube(datacube_id)
    assert isinstance(datacube, expected_datacube_class)


@pytest.mark.parametrize(
    ["datacube_id", "expected_datacube_class"],
    [
        [datacube_id, datacube_class]
        for datacube_id, datacube_class in assets.datacubes.items()
    ],
)
def test_get_datacube_class(
    datacube_id: str,
    expected_datacube_class: Type[GenericDatacube],
):
    datacube_class = get_datacube_class(datacube_id)
    assert datacube_class == expected_datacube_class


@pytest.mark.parametrize(
    ["catalog_class"],
    [[catalog_class] for catalog_class in list_of_catalog_classes],
)
def test_get_datacube_classes(catalog_class: Type[GenericCatalog]):
    datacube_class_list = get_datacube_classes(catalog_class)

    assert all(
        datacube_class.catalog.__class__ == catalog_class
        for datacube_class in datacube_class_list
    )
