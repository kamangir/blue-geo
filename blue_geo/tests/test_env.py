from abcli.tests.test_env import test_abcli_env
from blue_objects.tests.test_env import test_blue_objects_env

from blue_geo import env


def test_required_env():
    test_abcli_env()
    test_blue_objects_env()


def test_blue_geo_env():
    assert env.FIRMS_MAP_KEY
    assert env.COPERNICUS_AWS_ACCESS_KEY_ID
    assert env.COPERNICUS_AWS_SECRET_ACCESS_KEY
    assert env.BLUE_GEO_QGIS_TEMPLATE_FIRMS_AREA
    assert env.BLUE_GEO_QGIS_TEMPLATE_UKRAINE_TIMEMAP
    assert env.BLUE_GEO_QGIS_TEMPLATE_WATCH
    assert env.BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2
    assert env.BLUE_GEO_TEST_DATACUBE_CROP_CTULINE
    assert env.BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2_CHILCOTIN
    assert env.BLUE_GEO_TEST_DATACUBE_EARTHSEARCH_SENTINEL2_L1C
    assert env.BLUE_GEO_TEST_DATACUBE_FIRMS_AREA
    assert env.BLUE_GEO_TEST_DATACUBE_GENERIC_GENERIC
    assert env.BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP
