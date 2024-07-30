import os
from abcli.env import load_env, load_config

load_env(__name__)
load_config(__name__)


BLUE_GEO_UKRAINE_TIMEMAP_QGIS_TEMPLATE = os.getenv(
    "BLUE_GEO_UKRAINE_TIMEMAP_QGIS_TEMPLATE", ""
)

BLUE_GEO_FIRMS_AREA_QGIS_TEMPLATE = os.getenv(
    "BLUE_GEO_FIRMS_AREA_QGIS_TEMPLATE",
    "",
)

FIRMS_MAP_KEY = os.getenv("FIRMS_MAP_KEY", "")

QGIS_TEMPLATES = {
    "firms_area": BLUE_GEO_FIRMS_AREA_QGIS_TEMPLATE,
}

BLUE_GEO_TEST_DATACUBE_FIRMS_AREA = os.getenv(
    "BLUE_GEO_TEST_DATACUBE_FIRMS_AREA",
    "",
)
