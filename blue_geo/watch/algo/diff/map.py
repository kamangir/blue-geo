from typing import Dict
from tqdm import trange
import numpy as np
import cv2
import math

from blueness import module
from blue_options import string
from blue_objects.logger.matrix import log_matrix, log_matrix_hist
from blue_objects import file, objects
from blue_objects.metadata import post_to_object
from blue_objects.graphics.signature import add_signature

from blue_geo import NAME
from blue_geo.host import signature
from blue_geo.catalog.generic import GenericDatacube
from blue_geo.watch.workflow.common import load_watch
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def map_function(
    query_object_name: str,
    suffix: str,
    offset: str,
    depth: int,
    dynamic_range: float = 100.0,
    line_width: int = 80,
    colorbar_width: int = 20,
    min_width: int = 1200,
) -> bool:
    if depth < 2:
        logger.error(f"depth={depth} < 2!")
        return False

    offset_int = int(offset)

    object_name = f"{query_object_name}-{suffix}-{offset}"

    success, target, _ = load_watch(object_name, log=False)
    if not success:
        return success

    logger.info(
        "{}.map: {} #{}+D={} -> {}".format(
            NAME,
            target.one_liner,
            offset,
            depth,
            object_name,
        )
    )

    acquisition_metadata: Dict[str, Dict] = {}
    baseline_filename: str = ""
    target_filename: str = ""
    for index in trange(depth):
        logger.info(f"processing metadata: index={index} ...")

        index_object_name = "{}-D-{:03d}".format(
            object_name,
            offset_int + index,
        )
        success, acquisition_metadata[index] = file.load_yaml(
            objects.path_of(
                filename="metadata.yaml",
                object_name=index_object_name,
            ),
            ignore_error=True,
        )
        if not success:
            break

        if index in [0, 1]:
            filename = objects.path_of(
                filename=acquisition_metadata[index].get("map", {}).get("filename", ""),
                object_name=index_object_name,
            )
            if not file.exists(filename):
                logger.warning(f"{filename} not found!")
                success = False
                break

            if index == 0:
                baseline_filename = filename
            else:
                target_filename = filename

    baseline_metadata = {}
    if success:
        success, baseline_image, baseline_metadata = GenericDatacube.load_modality(
            filename=baseline_filename,
            modality="rgb",
            log=True,
        )

    if success:
        success, target_image, _ = GenericDatacube.load_modality(
            filename=target_filename,
            modality="rgb",
            log=True,
        )

    if success:
        diff_image = np.squeeze(
            target_image.astype(np.float32) - baseline_image.astype(np.float32)
        )
        diff_image[diff_image < -dynamic_range] = -dynamic_range
        diff_image[diff_image > dynamic_range] = dynamic_range

        diff_image_pretty_shape = string.pretty_shape_of_matrix(diff_image)

        success = file.save_matrix(
            objects.path_of(
                "{}-diff.npy".format(file.name(target_filename)),
                object_name,
            ),
            diff_image,
        )

    if success:
        log_matrix_hist(
            matrix=diff_image,
            dynamic_range=(-dynamic_range, dynamic_range),
            header=[
                "diff histogram",
                query_object_name,
                f"/{suffix}",
                f"offset: {offset}",
                f"depth: {depth}",
                file.name_and_extension(baseline_filename),
                file.name_and_extension(target_filename),
                diff_image_pretty_shape,
                "pixel_size: {} m".format(baseline_metadata.get("pixel_size", -1.0)),
            ],
            footer=["DN diff"],
            filename=objects.path_of(
                "{}-diff-histogram.png".format(file.name(target_filename)),
                object_name,
            ),
            line_width=line_width,
        )

    diff_filename = objects.path_of(
        "{}-diff.png".format(file.name(target_filename)),
        object_name,
    )
    if success:
        if not log_matrix(
            matrix=diff_image[:, :, 0],
            header=[
                " | ".join(
                    objects.signature(
                        " | ".join(
                            [
                                suffix,
                                f"offset: {offset}",
                                f"depth: {depth}",
                                file.name_and_extension(baseline_filename),
                                file.name_and_extension(target_filename),
                                diff_image_pretty_shape,
                                "pixel_size: {} m".format(
                                    baseline_metadata.get("pixel_size", -1.0)
                                ),
                            ]
                        ),
                        query_object_name,
                    )
                ),
            ],
            footer=[target.one_liner],
            filename=diff_filename,
            dynamic_range=(-dynamic_range, dynamic_range),
            line_width=line_width,
            min_width=min_width,
            colorbar_width=colorbar_width,
            colormap=cv2.COLORMAP_JET,
        ):
            success = False

    if not success:
        logger.warning("not usable.")

    return post_to_object(
        object_name,
        "map",
        {
            "algo": "diff",
            "inputs": {
                "offset": offset,
                "depth": depth,
                "acquisitions": acquisition_metadata,
            },
            "filename": file.name_and_extension(diff_filename),
            "target": target.__dict__,
            "usable": success,
        },
    )
