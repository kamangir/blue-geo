from abcli.tests import test_env
from blue_geo import env


def test_abcli_env():
    test_env.test_abcli_env()


def test_blue_geo_env():
    assert env.BLUE_GEO_UKRAINE_TIMEMAP_QGIS_TEMPLATE
    assert env.BLUE_GEO_FIRMS_AREA_QGIS_TEMPLATE
    assert env.FIRMS_MAP_KEY
