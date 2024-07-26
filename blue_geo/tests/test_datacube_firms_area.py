import pytest
import geopandas as gpd
from abcli.modules.objects import unique_object
from blue_geo.tests import assets
from blue_geo.catalog.firms.area import enums, FirmsAreaDatacube


@pytest.mark.parametrize(
    ["area", "source"],
    [
        [
            enums.Area.default(),
            enums.Source.default(),
        ],
    ],
)
def test_datacube_from_query(
    area: enums.Area,
    source: enums.Source,
):
    object_name = unique_object()

    datacube = FirmsAreaDatacube(area=area, source=source)

    assert datacube.description

    assert datacube.ingest_url()

    assert datacube.ingest_url(html=True)

    success, gdf = datacube.ingest(object_name)
    assert success
    assert isinstance(gdf, gpd.GeoDataFrame)

    assert datacube.datacube_id


@pytest.mark.parametrize(
    ["datacube_id"],
    [
        ["datacube-firms_area-world-MODIS_NRT-2024-07-20-1"],
    ],
)
def test_datacube_from_datacube_id(
    datacube_id: str,
):
    object_name = unique_object()

    datacube = FirmsAreaDatacube(datacube_id=datacube_id)

    assert datacube.description

    assert datacube.ingest_url()

    assert datacube.ingest_url(html=True)

    success, gdf = datacube.ingest(object_name)
    assert success
    assert isinstance(gdf, gpd.GeoDataFrame)

    assert datacube.datacube_id


@pytest.mark.parametrize(
    ["datacube_id", "expected_success"],
    assets.datacube_firms_area_parse_datacube_id,
)
def test_parse_datacube_id(
    datacube_id: str,
    expected_success: bool,
):
    success, segments = FirmsAreaDatacube.parse_datacube_id(datacube_id)
    assert success == expected_success
    if success:
        assert segments
