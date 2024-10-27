from typing import Dict
from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt

from blueness import module
from blue_options.host import signature as host_signature
from blue_objects import file, objects
from blue_objects.metadata import post_to_object, get_from_object
from blue_objects.graphics.signature import justify_text

from blue_geo import NAME, fullname
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
) -> bool:
    if depth < 2:
        logger.error(f"depth={depth} < 2!")
        return False

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

    success, target, _ = load_watch(object_name, log=False)
    if not success:
        return success

    logger.info(
        "{}.map: {} #{}+D={} @ {} -> {}".format(
            NAME,
            target.one_liner,
            offset,
            depth,
            datacube_id,
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
            )
        )
        if not success:
            return success

        if index in [0, 1]:
            filename = objects.path_of(
                filename=acquisition_metadata[index].get("map", {}).get("filename", ""),
                object_name=index_object_name,
            )
            if not file.exists(filename):
                logger.error(f"{filename} not found!")
                return False

            if index == 0:
                baseline_filename = filename
            else:
                target_filename = filename

    success, baseline_image, _ = GenericDatacube.load_modality(
        filename=baseline_filename,
        modality="rgb",
        log=True,
    )
    if not success:
        return success

    success, target_image, _ = GenericDatacube.load_modality(
        filename=target_filename,
        modality="rgb",
        log=True,
    )
    if not success:
        return success

    diff_image = np.squeeze(target_image[:, :, 0] - baseline_image[:, :, 0]).astype(
        np.float32
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
            " | ".join(
                [
                    "DN diff",
                    object_name,
                    fullname(),
                ]
                + host_signature()
            ),
            line_width=line_width,
            return_str=True,
        )
    )
    plt.ylabel("frequency")
    plt.grid(True)
    if not file.save_fig(
        objects.path_of("diff-histogram.png", object_name),
        log=True,
    ):
        return False

    # import ipdb

    # ipdb.set_trace()

    logger.info("🪄")

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
            "datacube_id": datacube_id,
            "target": target.__dict__,
            "usable": success,
        },
    )
