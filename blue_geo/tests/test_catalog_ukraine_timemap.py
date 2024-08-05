import pytest
import geopandas as gpd
from abcli.modules.objects import unique_object
from blue_geo.tests import assets
from blue_geo.catalog.ukraine_timemap import UkraineTimemapDatacube


@pytest.mark.parametrize(
    ["datacube_id"],
    [
        [
            [datacube_id]
            for datacube_id, datacube_class in assets.datacubes.items()
            if datacube_class == UkraineTimemapDatacube
        ][-1]
    ],
)
def test_datacube_from_datacube_id(datacube_id: str):
    object_name = unique_object()

    datacube = UkraineTimemapDatacube(datacube_id)

    assert datacube.datacube_id

    assert datacube.description

    success, df = datacube.ingest(object_name)
    assert success
    assert isinstance(df, gpd.GeoDataFrame)


@pytest.mark.parametrize(
    ["datacube_id", "expected_success"],
    [
        [datacube_id, datacube_class == UkraineTimemapDatacube]
        for datacube_id, datacube_class in assets.datacubes.items()
    ],
)
def test_parse_datacube_id(
    datacube_id: str,
    expected_success: bool,
):
    success, _ = UkraineTimemapDatacube.parse_datacube_id(datacube_id)
    assert success == expected_success
