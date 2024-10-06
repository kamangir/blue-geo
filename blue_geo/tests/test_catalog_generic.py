import pytest
from blue_geo.tests import assets
from blue_geo import env
from blue_geo.catalog.generic import GenericCatalog, GenericDatacube


def test_datacube():
    datacube = GenericDatacube(env.BLUE_GEO_TEST_DATACUBE_GENERIC_GENERIC)

    assert isinstance(datacube.catalog, GenericCatalog)

    assert datacube.datacube_id

    assert datacube.description

    assert datacube.raw

    success, _ = datacube.ingest()
    assert success


@pytest.mark.parametrize(
    ["datacube_id"],
    [
        [
            [datacube_id]
            for datacube_id, datacube_class in assets.datacubes.items()
            if datacube_class == GenericDatacube
        ][-1]
    ],
)
def test_datacube_from_datacube_id(datacube_id: str):
    datacube = GenericDatacube(datacube_id)

    assert datacube.datacube_id

    assert datacube.description

    success, _ = datacube.ingest()
    assert success


@pytest.mark.parametrize(
    ["datacube_id", "expected_success"],
    [
        [datacube_id, datacube_class == GenericDatacube]
        for datacube_id, datacube_class in assets.datacubes.items()
    ],
)
def test_parse_datacube_id(
    datacube_id: str,
    expected_success: bool,
):
    success, _ = GenericDatacube.parse_datacube_id(datacube_id)
    assert success == expected_success
