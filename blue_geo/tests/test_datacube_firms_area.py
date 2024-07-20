import pytest
import geopandas as gpd
from abcli.modules.objects import unique_object
from blue_geo.datacube.firms.area import enums, FirmsAreaDatacube


@pytest.mark.parametrize(
    ["area", "source"],
    [
        [
            enums.Area.default(),
            enums.Source.default(),
        ],
    ],
)
def test_datacube_firms_area(
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
