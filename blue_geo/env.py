import os
from blue_options.env import load_config, load_env, get_env

load_env(__name__)
load_config(__name__)


# secrets
FIRMS_MAP_KEY = get_env("FIRMS_MAP_KEY")

COPERNICUS_AWS_ACCESS_KEY_ID = get_env("COPERNICUS_AWS_ACCESS_KEY_ID")

COPERNICUS_AWS_SECRET_ACCESS_KEY = get_env("COPERNICUS_AWS_SECRET_ACCESS_KEY")

SKYFOX_ACCESS_TOKEN_URL = get_env("SKYFOX_ACCESS_TOKEN_URL")
SKYFOX_CLIENT_ID = get_env("SKYFOX_CLIENT_ID")
SKYFOX_CLIENT_SECRET = get_env("SKYFOX_CLIENT_SECRET")

# config

BLUE_GEO_DISABLED_CATALOGS = get_env("BLUE_GEO_DISABLED_CATALOGS")

BLUE_GEO_WATCH_TARGET_LIST = get_env("BLUE_GEO_WATCH_TARGET_LIST")

BLUE_GEO_SKYFOXCATALOG_API_URL = get_env("BLUE_GEO_SKYFOXCATALOG_API_URL")

BLUE_GEO_SKYFOXCATALOG_API_GET_TOKEN = get_env("BLUE_GEO_SKYFOXCATALOG_API_GET_TOKEN")

# QGIS templates
BLUE_GEO_QGIS_TEMPLATE_FIRMS_AREA = get_env("BLUE_GEO_QGIS_TEMPLATE_FIRMS_AREA")

BLUE_GEO_QGIS_TEMPLATE_DATACUBE_SKYFOX_VENUS = get_env(
    "BLUE_GEO_QGIS_TEMPLATE_DATACUBE_SKYFOX_VENUS"
)

BLUE_GEO_QGIS_TEMPLATE_UKRAINE_TIMEMAP = get_env(
    "BLUE_GEO_QGIS_TEMPLATE_UKRAINE_TIMEMAP"
)

BLUE_GEO_QGIS_TEMPLATE_WATCH = get_env("BLUE_GEO_QGIS_TEMPLATE_WATCH")


# test datacube-ids
BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2 = get_env(
    "BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2"
)
BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2_CHILCOTIN = get_env(
    "BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2_CHILCOTIN"
)

BLUE_GEO_TEST_DATACUBE_CROP_CTULINE = get_env("BLUE_GEO_TEST_DATACUBE_CROP_CTULINE")

BLUE_GEO_TEST_DATACUBE_EARTHSEARCH_SENTINEL2_L1C = get_env(
    "BLUE_GEO_TEST_DATACUBE_EARTHSEARCH_SENTINEL2_L1C"
)

BLUE_GEO_TEST_DATACUBE_FIRMS_AREA = get_env("BLUE_GEO_TEST_DATACUBE_FIRMS_AREA")

BLUE_GEO_TEST_DATACUBE_GENERIC_GENERIC = get_env(
    "BLUE_GEO_TEST_DATACUBE_GENERIC_GENERIC"
)

BLUE_GEO_TEST_DATACUBE_SKYFOX_VENUS = get_env("BLUE_GEO_TEST_DATACUBE_SKYFOX_VENUS")

BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP = get_env(
    "BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP"
)

BLUE_GEO_WATCH_ALGO_DIFF_MAP_DYNAMIC_RANGE = get_env(
    "BLUE_GEO_WATCH_ALGO_DIFF_MAP_DYNAMIC_RANGE"
)

BLUE_GEO_TEST_DATACUBE_MAXAR_OPEN_DATA = get_env(
    "BLUE_GEO_TEST_DATACUBE_MAXAR_OPEN_DATA"
)

BLUE_GEO_QGIS_TEMPLATE_MAXAR_OPEN_DATA = get_env(
    "BLUE_GEO_QGIS_TEMPLATE_MAXAR_OPEN_DATA"
)

MAXAR_OPEN_DATA_CLIENT_QUERY_RADIUS = get_env(
    "MAXAR_OPEN_DATA_CLIENT_QUERY_RADIUS", 0.01
)

MAXAR_OPEN_DATA_CLIENT_CACHE_ITEMS = get_env("MAXAR_OPEN_DATA_CLIENT_CACHE_ITEMS", True)

BLUE_GEO_PALISADES_TEST_DATACUBE = get_env("BLUE_GEO_PALISADES_TEST_DATACUBE")

BLUE_GEO_TEST_QUERY_OBJECT_PALISADES_MAXAR_TEST = get_env(
    "BLUE_GEO_TEST_QUERY_OBJECT_PALISADES_MAXAR_TEST"
)


BLUE_GEO_FILE_LOAD_GEOIMAGE_TEST_OBJECT = get_env(
    "BLUE_GEO_FILE_LOAD_GEOIMAGE_TEST_OBJECT"
)
BLUE_GEO_FILE_LOAD_GEOIMAGE_TEST_FILENAME = get_env(
    "BLUE_GEO_FILE_LOAD_GEOIMAGE_TEST_FILENAME"
)

BLUE_GEO_TEST_OBJECT = get_env("BLUE_GEO_TEST_OBJECT")
