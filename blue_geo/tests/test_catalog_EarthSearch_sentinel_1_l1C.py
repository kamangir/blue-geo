import pytest

from blue_objects.objects import unique_object

from blue_geo.tests import assets
from blue_geo.catalog.EarthSearch import EarthSearchCatalog
from blue_geo.catalog.EarthSearch.sentinel_2_l1c import EarthSearchSentinel2L1CDatacube


def test_get_list_of_collections():
    catalog = EarthSearchCatalog()
    assert catalog.get_list_of_collections()


def test_query():
    object_name = unique_object()

    success = EarthSearchSentinel2L1CDatacube.query(
        object_name,
        datetime="2024-07-30/2024-08-09",
        bbox=[-122.88, 51.73, -122.68, 51.93],
        count=5,
        verbose=True,
    )
    assert success


@pytest.mark.parametrize(
    ["datacube_id"],
    [
        [
            [datacube_id]
            for datacube_id, datacube_class in assets.datacubes.items()
            if datacube_class == EarthSearchSentinel2L1CDatacube
        ][-1]
    ],
)
def test_datacube_from_datacube_id(datacube_id: str):
    datacube = EarthSearchSentinel2L1CDatacube(datacube_id)

    success, _ = datacube.ingest()
    assert success

    assert datacube.list_of_files()


@pytest.mark.parametrize(
    ["datacube_id", "expected_success"],
    [
        [datacube_id, datacube_class == EarthSearchSentinel2L1CDatacube]
        for datacube_id, datacube_class in assets.datacubes.items()
    ],
)
def test_parse_datacube_id(
    datacube_id: str,
    expected_success: bool,
):
    success, _ = EarthSearchSentinel2L1CDatacube.parse_datacube_id(datacube_id)
    assert success == expected_success
