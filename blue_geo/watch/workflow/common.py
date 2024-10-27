from typing import Tuple, List
import glob
from functools import reduce

from blue_objects import objects

from blue_geo.watch.targets.target import Target
from blue_geo.catalog.generic.generic.scope import raster_suffix
from blue_geo.logger import logger


def load_watch(
    object_name: str,
    log: bool = True,
    list_of_suffix: List[str] = raster_suffix,
) -> Tuple[bool, Target, List[str]]:
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
                for suffix in list_of_suffix
            ],
        )
    )

    if log:
        logger.info("{} file(s) to process.".format(len(list_of_files)))

    return success, target, list_of_files
