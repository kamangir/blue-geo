from typing import Any, Dict, List
import numpy as np
import rasterio

from blue_options import string
from blue_objects.file.save import prepare_for_saving, finish_saving

from blue_objects import NAME


def save_geoimage(
    filename: str,
    image: np.ndarray,
    template_filename: str,
    log: bool = False,
    dtype: str = rasterio.float32,
):
    if not prepare_for_saving(filename):
        return False

    success = True
    try:
        with rasterio.open(template_filename) as src:
            profile = src.profile

            profile.update(
                dtype=dtype,
                count=image.shape[2],
                nodata=0,
            )
            with rasterio.open(filename, "w", **profile) as dst:
                dst.write(image)
    except:
        success = False

    return finish_saving(
        success,
        "{}.save_geoimage: {} -> {}".format(
            NAME,
            string.pretty_shape_of_matrix(image),
            filename,
        ),
        log,
    )
