from abcli.tests import test_env
from blue_geo import env


def test_abcli_env():
    test_env.test_abcli_env()


def test_blue_geo_env():
    assert env.UKRAINE_TIMEMAP_TEMPLATE
    assert env.FIRMS_MAP_KEY
