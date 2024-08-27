import glob
from tqdm import tqdm
from functools import reduce
from blueness import module
from abcli import file
from abcli.plugins.graphics.signature import add_signature
from abcli.plugins.graphics.gif import generate_animated_gif
from abcli.modules.host import signature as host_signature
from abcli.modules.objects import signature as header
from abcli.plugins.metadata import post_to_object
from abcli.modules import objects
from blue_geo import NAME, VERSION
from blue_geo import NAME as BLUE_GEO_NAME
from blue_geo.watch.targets import Target
from blue_geo.logger import logger
from typing import List


NAME = module.name(__file__, NAME)


def reduce_function(
    query_object_name: str,
    suffix: str,
    object_name: str,
) -> bool:
    success, target = Target.load(object_name)
    if not success:
        return success

    logger.info(
        "{}.reduce {}/{} @ {} -> {}".format(
            NAME,
            query_object_name,
            suffix,
            target,
            object_name,
        )
    )

    list_of_files = sorted(
        reduce(
            lambda x, y: x + y,
            [
                glob.glob(
                    objects.path_of(
                        f"*{suffix}",
                        object_name,
                    )
                )
                for suffix in [".jp2", ".tif", ".tiff"]
            ],
        )
    )
    logger.info("{} file(s) to process.".format(len(list_of_files)))

    bad_images: List[str] = []
    list_of_frames: List[str] = []
    for filename in tqdm(list_of_files):
        success, image = file.load_image(filename)
        if not success:
            bad_images.append(filename)
            continue

        image = add_signature(
            image,
            header=[
                " | ".join(header(file.name(filename), object_name)),
            ],
            footer=[
                str(target),
                " | ".join([f"{BLUE_GEO_NAME}.{VERSION}"] + host_signature()),
            ],
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
