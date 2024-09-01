import numpy as np
from blueness import module
from abcli import file
from abcli.plugins.metadata import post_to_object
from abcli import string
from blue_geo import NAME
from blue_geo.watch.workflow.common import load_watch
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def map_function(
    datacube_id: str,
    object_name: str,
    image_std_threshold: float = 0.1,
) -> bool:
    success, target, list_of_files = load_watch(object_name)
    if not success or not list_of_files:
        return success
    filename = list_of_files[0]

    success, image = file.load_image(filename)
    if not success:
        return success

    logger.info(
        "{}.map: {} @ {} -> {}".format(
            NAME,
            target,
            datacube_id,
            object_name,
        )
    )

    image = image.astype(np.float32) / 255.0
    image_mean = np.mean(image)
    image_std = np.std(image)

    image_is_valid = bool(image_std > image_std_threshold)

    logger.info(
        "{} image[{}]: {:.2f} {} {:.2f}".format(
            "✅" if image_is_valid else "🛑",
            string.pretty_shape_of_matrix(image),
            image_std,
            ">" if image_is_valid else "<=",
            image_std_threshold,
        )
    )

    return post_to_object(
        object_name,
        "map",
        {
            "activity": {
                "mean": image_mean.tolist(),
                "std": image_std.tolist(),
            },
            "datacube_id": datacube_id,
            "filename": file.name_and_extension(filename),
            "shape": list(image.shape),
            "target": target.__dict__,
            "valid": image_is_valid,
        },
    )
