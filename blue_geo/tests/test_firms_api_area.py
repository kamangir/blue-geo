import pytest
from blue_geo.firms.api.area import enums
from abcli.modules.objects import unique_object
from blue_geo.firms.api.area.classes import APIRequest
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

    api_request = APIRequest(area=area, source=source)

    assert api_request.as_str()

    assert api_request.url()

    assert api_request.url(html=True)

    success, gdf = api_request.ingest(object_name)
    assert success
    assert isinstance(gdf, gpd.GeoDataFrame)

    assert api_request.datacube_id
