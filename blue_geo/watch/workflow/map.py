import numpy as np

from blueness import module
from blue_options.host import signature as host_signature
from blue_objects import file, objects
from blue_objects.metadata import post_to_object
from blue_objects.graphics.signature import add_signature
from notebooks_and_scripts import NAME as NBS_NAME, VERSION as NBS_VERSION

from blue_geo import NAME, VERSION
from blue_geo import NAME as BLUE_GEO_NAME
from blue_geo.watch.workflow.common import load_watch
from blue_geo.catalog.functions import get_datacube_class
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def map_function(
    datacube_id: str,
    offset: int,
    modality: str,
    object_name: str,
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
    success, frame, frame_metadata = datacube_class.load_modality(
        filename,
        modality=modality,
        log=True,
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
            str(target),
            " | ".join(
                [f"{BLUE_GEO_NAME}.{VERSION}"]
                + [f"{NBS_NAME}.{NBS_VERSION}"]
                + host_signature()
            ),
        ],
        word_wrap=False,
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
            "metadata": frame_metadata,
            "target": target.__dict__,
            "usable": success,
        },
    )
