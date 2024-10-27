from typing import List, Dict
import glob
from tqdm import tqdm

from blueness import module
from blue_objects import file, objects
from blue_objects.graphics.gif import generate_animated_gif
from blue_objects.metadata import post_to_object

from blue_geo import NAME
from blue_geo.watch.workflow.common import load_watch
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def reduce_function(
    query_object_name: str,
    suffix: str,
    object_name: str,
) -> bool:
    success, target, list_of_files = load_watch(object_name)
    if not success:
        return success

    logger.info(
        "{}.reduce {}/{} @ {} -{} file(s)-> {}".format(
            NAME,
            query_object_name,
            suffix,
            target.one_liner,
            len(list_of_files),
            object_name,
        )
    )

    logger.info("🪄")

    return post_to_object(
        object_name,
        "reduce",
        {
            "algo": "diff",
            "list_of_files": [
                file.name_and_extension(filename) for filename in list_of_files
            ],
            "target": target.__dict__,
        },
    )
