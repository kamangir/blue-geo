from typing import Tuple, Any, Any, Dict
import numpy as np
import geopandas as gpd
import rasterio
import geojson

from blueness import module
from blue_options import string
from blue_options.logger import crash_report

from blue_geo import NAME
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


def load_geodataframe(
    filename: str,
    ignore_error: bool = False,
    log: bool = False,
) -> Tuple[bool, Any]:
    success = False
    gdf = None

    try:
        gdf = gpd.read_file(filename)
        success = True
    except:
        if not ignore_error:
            crash_report(f"{NAME}: load_geodataframe({filename}): failed.")

    if success and log:
        logger.info(
            "loaded {:,} rows: {} from {}".format(
                len(gdf),
                ", ".join(gdf.columns),
                filename,
            )
        )

    return success, gdf


def load_geoimage(
    filename: str,
    ignore_error: bool = False,
    log: bool = False,
) -> Tuple[bool, np.ndarray, Dict[str, Any]]:
    success = False
    image = np.empty((0,))
    pixel_size = -1.0
    crs = "unknown"

    try:
        with rasterio.open(filename) as src:
            image = src.read()

            pixel_size = src.res

            crs = src.crs

        success = True
    except:
        if not ignore_error:
            crash_report(f"{NAME}: load_geoimage({filename}): failed.")

    if success and log:
        logger.info(
            "loaded {} @ {} m : {} from {}".format(
                string.pretty_shape_of_matrix(image),
                pixel_size,
                crs,
                filename,
            )
        )

    return (
        success,
        image,
        {
            "pixel_size": pixel_size,
            "crs": crs,
        },
    )


# https://stackoverflow.com/a/47792385/17619982
def load_geojson(
    filename,
    ignore_error=False,
) -> Tuple[bool, Any]:
    success = False
    data = {}

    try:
        with open(filename, "r") as fh:
            data = geojson.load(fh)

        success = True
    except:
        if not ignore_error:
            crash_report(f"{NAME}: load_geojson({filename}): failed.")

    return success, data
