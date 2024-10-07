import numpy as np
import cv2
import math

from blueness import module
from blue_options import string
from blue_objects import file, objects
from blue_objects.metadata import post_to_object
from blue_objects.graphics.signature import add_signature

from blue_geo import NAME
from blue_geo.catalog.functions import get_datacube_class
from blue_geo.host import signature
from blue_geo.watch.workflow.common import load_watch
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def map_function(
    datacube_id: str,
    offset: int,
    modality: str,
    object_name: str,
    min_width: int = 1200,
) -> bool:
    success, target, list_of_files = load_watch(object_name)
    if not success or not list_of_files:
        return success
    filename = list_of_files[0]

    logger.info(
        "{}.map: {} #{} @ {} -{}-> {}".format(
            NAME,
            target,
            offset,
            datacube_id,
            modality,
            object_name,
        )
    )

    datacube_class = get_datacube_class(datacube_id)
    success, frame, _ = datacube_class.load_modality(
        filename,
        modality=modality,
        log=True,
    )

    if min_width != -1 and frame.shape[1] < min_width and frame.shape[1] > 0:
        scale = int(math.ceil(min_width / frame.shape[1]))

        logger.info(
            "scaling {} X {}".format(
                string.pretty_shape_of_matrix(frame),
                scale,
            )
        )

        frame = cv2.resize(
            frame,
            (
                scale * frame.shape[1],
                scale * frame.shape[0],
            ),
            interpolation=cv2.INTER_NEAREST_EXACT,
        )

    frame_fp32 = frame.astype(np.float32).flatten() / 255
    frame_fp32 = frame_fp32[frame_fp32 > 0.0]
    frame_fp32 = frame_fp32[frame_fp32 < 1.0]
    content_ratio = len(frame_fp32) / frame.size

    frame = add_signature(
        frame,
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
                    "{:05.1f}%".format(content_ratio * 100.0),
                    "#{:03d}".format(offset),
                ]
            ),
        ],
        footer=[
            target.one_liner,
            " | ".join(signature()),
        ],
        word_wrap=True,
    )

    frame_filename = file.add_extension(filename, "png")

    success = file.save_image(frame_filename, frame, log=True)

    return post_to_object(
        object_name,
        "map",
        {
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
