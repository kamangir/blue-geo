import os
from blue_options.env import load_config, load_env

load_env(__name__)
load_config(__name__)


# secrets
FIRMS_MAP_KEY = os.getenv(
    "FIRMS_MAP_KEY",
    "",
)

COPERNICUS_AWS_ACCESS_KEY_ID = os.getenv(
    "COPERNICUS_AWS_ACCESS_KEY_ID",
    "",
)

COPERNICUS_AWS_SECRET_ACCESS_KEY = os.getenv(
    "COPERNICUS_AWS_SECRET_ACCESS_KEY",
    "",
)

SKYFOX_ACCESS_TOKEN_URL = os.getenv(
    "SKYFOX_ACCESS_TOKEN_URL",
    "",
)
SKYFOX_CLIENT_ID = os.getenv(
    "SKYFOX_CLIENT_ID",
    "",
)
SKYFOX_CLIENT_SECRET = os.getenv(
    "SKYFOX_CLIENT_SECRET",
    "",
)

# config

BLUE_GEO_DISABLED_CATALOGS = os.getenv(
    "BLUE_GEO_DISABLED_CATALOGS",
    "",
)

BLUE_GEO_WATCH_TARGET_LIST = os.getenv(
    "BLUE_GEO_WATCH_TARGET_LIST",
    "",
)

BLUE_GEO_SKYFOXCATALOG_API_URL = os.getenv(
    "BLUE_GEO_SKYFOXCATALOG_API_URL",
    "",
)

BLUE_GEO_SKYFOXCATALOG_API_GET_TOKEN = os.getenv(
    "BLUE_GEO_SKYFOXCATALOG_API_GET_TOKEN",
    "",
)

# QGIS templates
BLUE_GEO_QGIS_TEMPLATE_FIRMS_AREA = os.getenv(
    "BLUE_GEO_QGIS_TEMPLATE_FIRMS_AREA",
    "",
)

BLUE_GEO_QGIS_TEMPLATE_DATACUBE_SKYFOX_VENUS = os.getenv(
    "BLUE_GEO_QGIS_TEMPLATE_DATACUBE_SKYFOX_VENUS",
    "",
)

BLUE_GEO_QGIS_TEMPLATE_UKRAINE_TIMEMAP = os.getenv(
    "BLUE_GEO_QGIS_TEMPLATE_UKRAINE_TIMEMAP",
    "",
)

BLUE_GEO_QGIS_TEMPLATE_WATCH = os.getenv(
    "BLUE_GEO_QGIS_TEMPLATE_WATCH",
    "",
)


# test datacube-ids
BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2 = os.getenv(
    "BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2",
    "",
)
BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2_CHILCOTIN = os.getenv(
    "BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2_CHILCOTIN",
    "",
)

BLUE_GEO_TEST_DATACUBE_CROP_CTULINE = os.getenv(
    "BLUE_GEO_TEST_DATACUBE_CROP_CTULINE",
    "",
)

BLUE_GEO_TEST_DATACUBE_EARTHSEARCH_SENTINEL2_L1C = os.getenv(
    "BLUE_GEO_TEST_DATACUBE_EARTHSEARCH_SENTINEL2_L1C",
    "",
)

BLUE_GEO_TEST_DATACUBE_FIRMS_AREA = os.getenv(
    "BLUE_GEO_TEST_DATACUBE_FIRMS_AREA",
    "",
)

BLUE_GEO_TEST_DATACUBE_GENERIC_GENERIC = os.getenv(
    "BLUE_GEO_TEST_DATACUBE_GENERIC_GENERIC",
    "",
)

BLUE_GEO_TEST_DATACUBE_SKYFOX_VENUS = os.getenv(
    "BLUE_GEO_TEST_DATACUBE_SKYFOX_VENUS",
    "",
)

BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP = os.getenv(
    "BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP",
    "",
)

BLUE_GEO_WATCH_ALGO_DIFF_MAP_DYNAMIC_RANGE = os.getenv(
    "BLUE_GEO_WATCH_ALGO_DIFF_MAP_DYNAMIC_RANGE",
    "250.0",
)

BLUE_GEO_TEST_DATACUBE_MAXAR_OPEN_DATA = os.getenv(
    "BLUE_GEO_TEST_DATACUBE_MAXAR_OPEN_DATA",
    "",
)

BLUE_GEO_QGIS_TEMPLATE_MAXAR_OPEN_DATA = os.getenv(
    "BLUE_GEO_QGIS_TEMPLATE_MAXAR_OPEN_DATA",
    "",
)
