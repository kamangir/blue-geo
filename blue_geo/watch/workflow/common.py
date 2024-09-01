from typing import Tuple, List
import glob
from functools import reduce
from abcli.modules import objects
from blue_geo.watch.targets import Target
from blue_geo.logger import logger


def load_watch(object_name: str) -> Tuple[bool, Target, List[str]]:
    success, target = Target.load(object_name)

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

    return success, target, list_of_files
