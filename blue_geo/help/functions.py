from typing import List
from blue_geo.help.datacube import get as get_datacube
from blue_geo.help.gdal import get as get_gdal
from blue_geo.help.QGIS import get as get_QGIS


def get(
    tokens: List[str],
    mono: bool,
) -> str:
    if tokens[0] == "datacube":
        return get_datacube(tokens[1:], mono=mono)

    if tokens[0] == "gdal":
        return get_gdal(tokens[1:], mono=mono)

    if tokens[0] == "QGIS":
        return get_QGIS(tokens[1:], mono=mono)

    return ""
