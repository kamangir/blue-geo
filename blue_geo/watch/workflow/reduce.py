from typing import List, Dict
from tqdm import tqdm
import numpy as np
from blueness import module
from abcli import string
from abcli import file
from abcli.plugins.graphics.signature import add_signature
from abcli.plugins.graphics.gif import generate_animated_gif
from abcli.modules.host import signature as host_signature
from abcli.modules.objects import signature as header
from abcli.plugins.metadata import post_to_object
from abcli.modules import objects
from blue_geo import NAME, VERSION
from blue_geo import NAME as BLUE_GEO_NAME
from notebooks_and_scripts import NAME as NBS_NAME, VERSION as NBS_VERSION
from blue_geo.watch.workflow.common import load_watch
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def reduce_function(
    query_object_name: str,
    suffix: str,
    object_name: str,
    image_std_threshold: float = 0.02,
    image_content_threshold: float = 0.5,
) -> bool:
    success, target, list_of_files = load_watch(object_name)
    if not success:
        return success

    logger.info(
        "{}.reduce {}/{} @ {} -{} file(s)-> {}".format(
            NAME,
            query_object_name,
            suffix,
            target,
            len(list_of_files),
            object_name,
        )
    )

    bad_images: List[str] = []
    invalid_images: List[str] = []
    list_of_frames: List[str] = []
    frame_metadata: Dict[str:Dict] = {}
    for filename in tqdm(list_of_files):
        success, image = file.load_image(filename)
        if not success:
            bad_images.append(filename)
            continue

        image_fp32 = image.astype(np.float32).flatten() / 255.0
        image_fp32 = image_fp32[image_fp32 > 0.0]
        image_fp32 = image_fp32[image_fp32 < 1.0]
        image_std = np.std(image_fp32) if image_fp32.size else 0.0
        image_content_ratio = len(image_fp32) / image.size

        image_is_valid = bool(
            image_std > image_std_threshold
            and image_content_ratio > image_content_threshold
        )
        logger.info(
            "{} image[{}]: std={:.03f} <?> {:.03f}, content={:.03f} <?> {:.03f}".format(
                "✅" if image_is_valid else "🛑",
                string.pretty_shape_of_matrix(image),
                image_std,
                image_std_threshold,
                image_content_ratio,
                image_content_threshold,
            )
        )
        frame_metadata[file.name_and_extension(filename)] = {
            "content": float(image_content_ratio),
            "shape": list(image.shape),
            "std": float(image_std),
            "valid": image_is_valid,
        }
        if not image_is_valid:
            invalid_images.append(filename)
            continue

        image = add_signature(
            image,
            header=[
                " | ".join(
                    header(file.name(filename), object_name)
                    + [
                        "std: {:.03f}".format(image_std),
                        "{:0.2f}%".format(image_content_ratio * 100.0),
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

        frame_filename = file.set_extension(filename, "png")
        if not file.save_image(frame_filename, image):
            bad_images.append(frame_filename)
        else:
            list_of_frames.append(frame_filename)

    if not post_to_object(
        object_name,
        "reduce",
        {
            "bad_images": bad_images,
            "frames": frame_metadata,
            "invalid_images": invalid_images,
            "list_of_files": [
                file.name_and_extension(filename) for filename in list_of_files
            ],
            "target": target.__dict__,
        },
    ):
        return False

    return generate_animated_gif(
        list_of_frames,
        objects.path_of(
            f"{object_name}.gif",
            object_name,
        ),
        frame_duration=1000,
    )
