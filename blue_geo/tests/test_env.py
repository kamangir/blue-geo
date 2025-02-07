from abcli.tests.test_env import test_abcli_env
from blue_objects.tests.test_env import test_blue_objects_env

from blue_geo import env


def test_required_env():
    test_abcli_env()
    test_blue_objects_env()


def test_blue_geo_env():
    assert env.FIRMS_MAP_KEY

    assert env.BLUE_GEO_SKYFOXCATALOG_API_URL
    assert env.BLUE_GEO_SKYFOXCATALOG_API_GET_TOKEN

    assert env.COPERNICUS_AWS_ACCESS_KEY_ID
    assert env.COPERNICUS_AWS_SECRET_ACCESS_KEY

    assert env.BLUE_GEO_QGIS_TEMPLATE_FIRMS_AREA
    assert env.BLUE_GEO_QGIS_TEMPLATE_DATACUBE_SKYFOX_VENUS
    assert env.BLUE_GEO_QGIS_TEMPLATE_UKRAINE_TIMEMAP
    assert env.BLUE_GEO_QGIS_TEMPLATE_WATCH
    assert env.BLUE_GEO_QGIS_TEMPLATE_MAXAR_OPEN_DATA

    assert env.BLUE_GEO_WATCH_TARGET_LIST

    assert env.BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2
    assert env.BLUE_GEO_TEST_DATACUBE_CROP_CTULINE
    assert env.BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2_CHILCOTIN
    assert env.BLUE_GEO_TEST_DATACUBE_EARTHSEARCH_SENTINEL2_L1C
    assert env.BLUE_GEO_TEST_DATACUBE_FIRMS_AREA
    assert env.BLUE_GEO_TEST_DATACUBE_GENERIC_GENERIC
    assert env.BLUE_GEO_TEST_DATACUBE_SKYFOX_VENUS
    assert env.BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP
    assert env.BLUE_GEO_TEST_DATACUBE_MAXAR_OPEN_DATA

    assert env.SKYFOX_ACCESS_TOKEN_URL
    assert env.SKYFOX_CLIENT_ID
    assert env.SKYFOX_CLIENT_SECRET

    assert env.BLUE_GEO_WATCH_ALGO_DIFF_MAP_DYNAMIC_RANGE

    assert env.MAXAR_OPEN_DATA_CLIENT_QUERY_RADIUS != 0.0
    assert isinstance(env.MAXAR_OPEN_DATA_CLIENT_CACHE_ITEMS, bool)

    assert env.BLUE_GEO_PALISADES_TEST_DATACUBE

    assert env.BLUE_GEO_TEST_QUERY_OBJECT_PALISADES_MAXAR_TEST

    assert env.BLUE_GEO_FILE_LOAD_GEOIMAGE_TEST_OBJECT
    assert env.BLUE_GEO_FILE_LOAD_GEOIMAGE_TEST_FILENAME

    assert env.BLUE_GEO_TEST_OBJECT
