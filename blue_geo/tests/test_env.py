from abcli.tests import test_env
from blue_geo import env


def test_abcli_env():
    test_env.test_abcli_env()


def test_blue_geo_env():
    assert env.BLUE_GEO_UKRAINE_TIMEMAP_QGIS_TEMPLATE
    assert env.BLUE_GEO_FIRMS_AREA_QGIS_TEMPLATE
    assert env.FIRMS_MAP_KEY
    assert env.COPERNICUS_AWS_ACCESS_KEY_ID
    assert env.COPERNICUS_AWS_SECRET_ACCESS_KEY
    assert env.BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2
    assert env.BLUE_GEO_TEST_DATACUBE_FIRMS_AREA
    assert env.BLUE_GEO_TEST_DATACUBE_GENERIC_GENERIC
    assert env.BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP
