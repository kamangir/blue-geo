from typing import Tuple
from abcli import string
from blue_geo.logger import logger

raster_suffix = [
    ".jp2",
    ".tif",
    ".tiff",
]


class DatacubeScope:
    special_options = ["all", "metadata", "quick", "raster"]

    help = "|".join(special_options + ["<{}>".format("+".join(raster_suffix))])

    def __init__(self, what: str):
        list_of_what = what.split("+")

        self.all = "all" in list_of_what

        self.metadata = "metadata" in list_of_what

        self.quick = "quick" in list_of_what

        self.raster = "raster" in list_of_what

        self.suffix = [
            item for item in list_of_what if item not in self.special_options
        ]

    def includes(
        self,
        item_filename: str,
        item_size: int = -1,
        verbose: bool = False,
        quick_found: bool = False,
    ) -> Tuple[bool, bool]:
        if self.all:
            return True, quick_found

        if (
            self.metadata
            and item_size <= 10**6
            and not any(item_filename.endswith(suffix) for suffix in raster_suffix)
        ):
            return True, quick_found

        if (
            self.quick
            and not quick_found
            and item_filename.endswith(".jp2")
            and "TCI" in item_filename
        ):
            return True, True

        if self.raster and any(
            item_filename.endswith(suffix) for suffix in raster_suffix
        ):
            return True, quick_found

        if self.suffix and any(
            item_filename.endswith(suffix) for suffix in self.suffix
        ):
            return True, quick_found

        if verbose:
            logger.info(
                "skipped {}: {}".format(
                    string.pretty_bytes(item_size),
                    item_filename,
                )
            )

        return False, quick_found
