import pytest

from blue_objects.objects import unique_object

from blue_geo.tests import assets
from blue_geo.catalog.maxar_open_data import MaxarOpenDataCatalog, MaxarOpenDataDatacube


def test_get_list_of_collections():
    catalog = MaxarOpenDataCatalog()
    assert catalog.get_list_of_collections()


@pytest.mark.parametrize(
    ["lat", "lon"],
    [
        [-1, -1],
        [34.2160393, -118.1509575],
    ],
)
def test_query(
    lat: float,
    lon: float,
):
    object_name = unique_object()

    success = MaxarOpenDataDatacube.query(
        object_name=object_name,
        collection_id="WildFires-LosAngeles-Jan-2025",
        lat=lat,
        lon=lon,
        start_date="2025-01-10",
        end_date="2025-01-13",
        count=3,
    )
    assert success


@pytest.mark.parametrize(
    ["datacube_id"],
    [
        [
            [datacube_id]
            for datacube_id, datacube_class in assets.datacubes.items()
            if datacube_class == MaxarOpenDataDatacube
        ][-1]
    ],
)
def test_datacube_from_datacube_id(datacube_id: str):
    datacube = MaxarOpenDataDatacube(datacube_id)

    success, _ = datacube.ingest()
    assert success

    assert datacube.list_of_files()


@pytest.mark.parametrize(
    ["datacube_id", "expected_success"],
    [
        [datacube_id, datacube_class == MaxarOpenDataDatacube]
        for datacube_id, datacube_class in assets.datacubes.items()
    ],
)
def test_parse_datacube_id(
    datacube_id: str,
    expected_success: bool,
):
    success, _ = MaxarOpenDataDatacube.parse_datacube_id(datacube_id)
    assert success == expected_success
