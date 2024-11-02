from typing import Dict
from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt
import cv2

from blueness import module
from blue_objects import file, objects
from blue_objects.metadata import post_to_object
from blue_objects.graphics.signature import justify_text, add_signature

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
    diff_range: float = 100,
    line_width: int = 80,
    colorbar_width: int = 20,
) -> bool:
    diff_filename: str = ""
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

    if success:
        success, baseline_image, _ = GenericDatacube.load_modality(
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
            target_image[:, :, 0].astype(np.float32)
            - baseline_image[:, :, 0].astype(np.float32)
        )
        diff_image[diff_image < -diff_range] = -diff_range
        diff_image[diff_image > diff_range] = diff_range

        plt.figure(figsize=(10, 6))
        plt.hist(
            diff_image.ravel(),
            bins=256,
            range=(-diff_range, diff_range),
        )
        plt.title(
            justify_text(
                " | ".join(
                    [
                        "diff histogram",
                        query_object_name,
                        f"/{suffix}",
                        f"@{offset}+{depth}",
                        f"+-{diff_range:.2f}",
                        file.name_and_extension(baseline_filename),
                        file.name_and_extension(target_filename),
                    ]
                ),
                line_width=line_width,
                return_str=True,
            )
        )
        plt.xlabel(
            justify_text(
                " | ".join(["DN diff"] + signature()),
                line_width=line_width,
                return_str=True,
            )
        )
        plt.ylabel("frequency")
        plt.grid(True)
        success = file.save_fig(
            objects.path_of(
                "{}-diff-histogram.png".format(file.name(target_filename)),
                object_name,
            ),
            log=True,
        )

    if success:
        colored_diff = cv2.applyColorMap(
            ((diff_image / diff_range + 1) / 2 * 255).astype(np.uint8), cv2.COLORMAP_JET
        )

        gradient = (
            255
            * np.linspace(0, 1, colored_diff.shape[0]).reshape(-1, 1)
            * np.ones((1, colorbar_width))
        ).astype(np.uint8)
        colorbar = cv2.applyColorMap(gradient, cv2.COLORMAP_JET)
        concatenated_image = np.hstack(
            (
                colored_diff,
                np.zeros(
                    (colored_diff.shape[0], colorbar_width // 2, 3),
                    dtype=np.uint8,
                ),
                colorbar,
            )
        )
        colored_diff_signed = add_signature(
            concatenated_image,
            header=[
                " | ".join(
                    objects.signature(
                        " | ".join(
                            [
                                suffix,
                                f"@{offset}+{depth}",
                                f"+-{diff_range:.2f}",
                                file.name_and_extension(baseline_filename),
                                file.name_and_extension(target_filename),
                            ]
                        ),
                        query_object_name,
                    )
                ),
            ],
            footer=[
                target.one_liner,
                " | ".join(signature()),
            ],
            word_wrap=True,
        )
        diff_filename = objects.path_of(
            "{}-diff.png".format(file.name(target_filename)),
            object_name,
        )
        success = file.save_image(
            diff_filename,
            colored_diff_signed,
            log=True,
        )

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
