from typing import Tuple, Dict, List, Union, Callable

from blue_options import string

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

    def filter(
        self,
        dict_of_items: Dict[str, float],  # {filename: size}
        verbose: bool = False,
        needed_for_quick: Union[Callable, None] = None,
    ) -> List[str]:
        list_of_files: List[str] = []

        for item_filename, item_size in dict_of_items.items():
            if self.includes(
                item_filename=item_filename,
                item_size=item_size,
                verbose=verbose,
                needed_for_quick=needed_for_quick,
            ):
                list_of_files.append(item_filename)

        return list_of_files

    def includes(
        self,
        item_filename: str,
        item_size: int = -1,
        verbose: bool = False,
        needed_for_quick: Union[Callable, None] = None,
    ) -> bool:
        if self.all:
            return True

        if (
            self.metadata
            and item_size <= 10**6
            and not any(item_filename.endswith(suffix) for suffix in raster_suffix)
        ):
            return True

        if (
            self.quick
            and (needed_for_quick is not None)
            and needed_for_quick(item_filename)
        ):
            return True

        if self.raster and any(
            item_filename.endswith(suffix) for suffix in raster_suffix
        ):
            return True

        if self.suffix and any(
            item_filename.endswith(suffix) for suffix in self.suffix
        ):
            return True

        if verbose:
            logger.info(
                "skipped {}: {}".format(
                    string.pretty_bytes(item_size),
                    item_filename,
                )
            )

        return False
