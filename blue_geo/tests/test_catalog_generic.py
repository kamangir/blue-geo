from typing import Type
import pytest
from abcli.modules.objects import unique_object
from blue_geo.tests import assets
from blue_geo.catalog.generic import GenericCatalog, VoidCatalog


@pytest.mark.parametrize(
    ["catalog_class"],
    [
        [
            GenericCatalog,
            VoidCatalog,
        ],
    ],
)
def test_catalog(catalog_class: Type[GenericCatalog]):
    catalog = catalog_class()
    assert catalog.name
