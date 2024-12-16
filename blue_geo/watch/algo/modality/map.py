import numpy as np

from blueness import module
from blue_objects import file, objects
from blue_objects.logger.matrix import log_matrix
from blue_objects.metadata import post_to_object, get_from_object
from blueflow import fullname as blueflow_fullname

from blue_geo import fullname
from blue_geo import NAME
from blue_geo.catalog.functions import get_datacube_class
from blue_geo.watch.workflow.common import load_watch
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def map_function(
    query_object_name: str,
    suffix: str,
    offset: str,
    modality: str,
    line_width: int = 80,
    min_width: int = 1200,
) -> bool:
    offset_int = int(offset)

    object_name = f"{query_object_name}-{suffix}-{offset}"

    list_of_datacube_id = get_from_object(
        query_object_name,
        "datacube_id",
        [],
    )
    if len(list_of_datacube_id) < offset_int + 1:
        logger.warning(f"offset={offset}: datacube-id not found.")
        return True
    datacube_id = list_of_datacube_id[offset_int]

    success, target, list_of_files = load_watch(object_name)
    if not success or not list_of_files:
        return success
    filename = list_of_files[0]

    logger.info(
        "{}.map: {} #{} @ {} -{}-> {}".format(
            NAME,
            target.one_liner,
            offset,
            datacube_id,
            modality,
            object_name,
        )
    )

    datacube_class = get_datacube_class(datacube_id)
    success, frame, frame_file_metadata = datacube_class.load_geoimage(
        filename,
        log=True,
    )

    if not file.save_matrix(
        file.add_extension(filename, "npy"),
        frame,
    ):
        success = False

    if frame.dtype == np.uint16:
        frame = frame.astype(np.float32) / 5000 * 255
        frame[frame < 0] = 0
        frame[frame > 255] = 255
        frame = frame.astype(np.uint8)

    frame_fp32 = frame.astype(np.float32).flatten() / 255
    frame_fp32 = frame_fp32[frame_fp32 > 0.0]
    frame_fp32 = frame_fp32[frame_fp32 < 1.0]
    content_ratio = len(frame_fp32) / frame.size

    if not log_matrix(
        matrix=frame,
        header=[
            " | ".join(
                objects.signature(
                    "{} / {}".format(
                        datacube_id,
                        file.name_and_extension(filename),
                    ),
                    object_name,
                )
                + [
                    "crs: {}".format(frame_file_metadata.get("crs", "?")),
                    "pixel size: {}".format(
                        frame_file_metadata.get("pixel_size", -1.0)
                    ),
                    "content: {:05.1f}%".format(content_ratio * 100.0),
                    f"#{offset}",
                ]
            ),
        ],
        footer=[
            target.one_liner,
            fullname(),
            blueflow_fullname(),
        ],
        filename=file.add_extension(filename, "png"),
        line_width=line_width,
        min_width=min_width,
    ):
        success = False

    return post_to_object(
        object_name,
        "map",
        {
            "algo": "modality",
            "inputs": {
                "offset": offset,
                "modality": modality,
            },
            "content_ratio": content_ratio,
            "datacube_id": datacube_id,
            "filename": file.name_and_extension(filename),
            "target": target.__dict__,
            "usable": success,
        },
    )
