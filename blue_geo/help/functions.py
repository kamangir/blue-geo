from typing import List
from blue_geo.help.catalog import get as get_catalog
from blue_geo.help.datacube import get as get_datacube
from blue_geo.help.gdal import get as get_gdal
from blue_geo.help.QGIS import get as get_QGIS


def get(
    tokens: List[str],
    mono: bool,
) -> str:
    for token, func in {
        "catalog": get_catalog,
        "datacube": get_datacube,
        "gdal": get_gdal,
        "QGIS": get_QGIS,
    }.items():
        if tokens[0] == token:
            return func(tokens[1:], mono=mono)

    return ""
