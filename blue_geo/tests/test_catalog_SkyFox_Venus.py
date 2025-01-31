import pytest

from blue_objects.objects import unique_object

from blue_geo.tests import assets
from blue_geo.catalog.SkyFox.Venus import SkyFoxVenusDatacube
from blue_geo.catalog.SkyFox.classes import SkyFoxCatalog


def test_SkyFoxCatalog_token():
    success, token = SkyFoxCatalog.get_new_token()
    assert success
    assert token


def test_get_list_of_collections():
    catalog = SkyFoxCatalog()
    assert catalog.get_list_of_collections()


@pytest.mark.skip(reason="SkyFox issue expected.")
def test_query():
    object_name = unique_object()

    success = SkyFoxVenusDatacube.query(
        object_name=object_name,
        bbox=[12.2389 - 0.1, 41.8003 - 0.1, 12.2389 + 0.1, 41.8003 + 0.1],
        datetime="2019-12-13/2020-10-28",
        count=5,
        verbose=True,
    )
    assert success


@pytest.mark.skip(reason="SkyFox issue expected.")
@pytest.mark.parametrize(
    ["datacube_id"],
    [
        (
            [
                [datacube_id]
                for datacube_id, datacube_class in assets.datacubes.items()
                if datacube_class == SkyFoxVenusDatacube
            ]
            + [["void"]]
        )[-1]
    ],
)
def test_datacube_from_datacube_id(datacube_id: str):
    datacube = SkyFoxVenusDatacube(datacube_id)

    success, _ = datacube.ingest()
    assert success

    assert isinstance(datacube.generate("rgb"), str)

    assert datacube.list_of_files()


@pytest.mark.parametrize(
    ["datacube_id", "expected_success"],
    [
        [datacube_id, datacube_class == SkyFoxVenusDatacube]
        for datacube_id, datacube_class in assets.datacubes.items()
    ],
)
def test_parse_datacube_id(
    datacube_id: str,
    expected_success: bool,
):
    success, _ = SkyFoxVenusDatacube.parse_datacube_id(datacube_id)
    assert success == expected_success
