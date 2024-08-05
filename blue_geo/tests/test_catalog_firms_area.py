import pytest
import geopandas as gpd
from abcli.modules.objects import unique_object
from blue_geo.tests import assets
from blue_geo.catalog.firms import FirmsCatalog
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

    assert isinstance(datacube.catalog, FirmsCatalog)

    assert datacube.datacube_id

    assert datacube.description

    assert datacube.ingest_url()

    assert datacube.ingest_url(html=True)

    success, gdf = datacube.ingest(object_name)
    assert success
    assert isinstance(gdf, gpd.GeoDataFrame)


@pytest.mark.parametrize(
    ["datacube_id"],
    [
        [
            [datacube_id]
            for datacube_id, datacube_class in assets.datacubes.items()
            if datacube_class == FirmsAreaDatacube
        ][-1]
    ],
)
def test_datacube_from_datacube_id(datacube_id: str):
    object_name = unique_object()

    datacube = FirmsAreaDatacube(datacube_id)

    assert datacube.datacube_id

    assert datacube.description

    success, df = datacube.ingest(object_name)
    assert success
    assert isinstance(df, gpd.GeoDataFrame)


@pytest.mark.parametrize(
    ["datacube_id", "expected_success"],
    [
        [datacube_id, datacube_class == FirmsAreaDatacube]
        for datacube_id, datacube_class in assets.datacubes.items()
    ],
)
def test_parse_datacube_id(
    datacube_id: str,
    expected_success: bool,
):
    success, _ = FirmsAreaDatacube.parse_datacube_id(datacube_id)
    assert success == expected_success
