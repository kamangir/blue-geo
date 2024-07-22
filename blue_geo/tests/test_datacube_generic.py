import pytest
from abcli.modules.objects import unique_object
from blue_geo.tests import assets
from blue_geo.datacube.generic import GenericDatacube


def test_datacube():
    object_name = unique_object()

    datacube = GenericDatacube()

    assert datacube.datacube_id

    assert datacube.description

    success, _ = datacube.ingest(object_name)
    assert success


@pytest.mark.parametrize(
    ["datacube_id"],
    [
        ["datacube-generic"],
    ],
)
def test_datacube_from_datacube_id(datacube_id: str):
    object_name = unique_object()

    datacube = GenericDatacube(datacube_id)

    assert datacube.datacube_id

    assert datacube.description

    success, _ = datacube.ingest(object_name)
    assert success


@pytest.mark.parametrize(
    ["datacube_id", "expected_success"],
    assets.datacube_generic_parse_datacube_id,
)
def test_parse_datacube_id(
    datacube_id: str,
    expected_success: bool,
):
    success, _ = GenericDatacube.parse_datacube_id(datacube_id)
    assert success == expected_success
