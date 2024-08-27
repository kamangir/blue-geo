import pytest
import geopandas as gpd
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
    datacube = UkraineTimemapDatacube(datacube_id)

    assert datacube.datacube_id

    assert datacube.description

    success, df = datacube.ingest()
    assert success
    assert isinstance(df, gpd.GeoDataFrame)

    assert datacube.list_of_files()


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
