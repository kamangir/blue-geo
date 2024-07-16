import pytest
from blue_geo.firms.api.area import enums
from blue_geo.firms.api.area.classes import APIRequest


@pytest.mark.parametrize(
    ["area", "source"],
    [
        [
            enums.Area.WORLD,
            enums.Source.MODIS_NRT,
        ],
    ],
)
def test_blue_geo_firms_api_area(
    area: enums.Area,
    source: enums.Source,
):
    api_request = APIRequest(area=area, source=source)

    assert api_request.as_str()

    assert api_request.url()

    assert api_request.url(html=True)
