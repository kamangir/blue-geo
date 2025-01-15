from typing import List
import json
import numpy as np

from blueness import module
from blue_objects import file, objects
from blue_objects.logger.matrix import log_matrix
from blueflow import fullname as blueflow_fullname

from blue_geo import fullname

from blue_geo import NAME

NAME = module.name(__file__, NAME)


def log_geoimage(
    object_name: str,
    filename: str,
    header: List[str] = [],
    footer: List[str] = [],
    log: bool = True,
    verbose: bool = True,
    **kwargs,
) -> bool:
    full_filename = objects.path_of(
        filename=filename,
        object_name=object_name,
    )

    success, matrix, metadata = file.load_geoimage(
        full_filename,
        log=log,
    )
    if not success:
        return success

    matrix = np.transpose(matrix, (1, 2, 0))

    metadata_as_str: List[str] = []
    try:
        for keyword, value in metadata.items():
            try:
                metadata_as_str += [f"{keyword}={json.dumps(value)}"]
            except Exception:
                metadata_as_str += [f"{keyword}=..."]
    except Exception:
        pass

    return log_matrix(
        matrix=matrix,
        filename=file.add_extension(full_filename, "png"),
        header=objects.signature(
            info=filename,
            object_name=object_name,
        )
        + metadata_as_str
        + header,
        footer=[
            fullname(),
            blueflow_fullname(),
        ]
        + footer,
        log=log,
        verbose=verbose,
        **kwargs,
    )
