import pytest
from blue_geo.firms.api.area import enums
from abcli.modules.objects import unique_object
from blue_geo.firms.api.area.classes import FirmsDatacube
import geopandas as gpd


@pytest.mark.parametrize(
    ["area", "source"],
    [
        [
            enums.Area.default(),
            enums.Source.default(),
        ],
    ],
)
def test_blue_geo_firms_api_area(
    area: enums.Area,
    source: enums.Source,
):
    object_name = unique_object()

    datacube = FirmsDatacube(area=area, source=source)

    assert datacube.description

    assert datacube.url()

    assert datacube.url(html=True)

    success, gdf = datacube.ingest(object_name)
    assert success
    assert isinstance(gdf, gpd.GeoDataFrame)

    assert datacube.datacube_id
