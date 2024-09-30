from typing import Tuple, Dict, List, Union, Callable, Any

from blue_options import string

from blue_geo.logger import logger

raster_suffix = [
    ".jp2",
    ".tif",
    ".tiff",
]


class DatacubeScope:
    # description under blue_geo_datacube_ingest
    special_options = [
        "all",
        "metadata",
        "raster",
        "rgb",
        "rgbx",
    ]

    help = "+".join(
        sorted(special_options) + [f"<{suffix}>" for suffix in raster_suffix]
    )

    def __init__(self, what: str):
        list_of_what = what.split("+")

        self.all = "all" in list_of_what

        self.metadata = "metadata" in list_of_what

        self.rgb = "rgb" in list_of_what
        self.rgbx = "rgbx" in list_of_what

        self.raster = "raster" in list_of_what

        self.suffix = [
            item for item in list_of_what if item not in self.special_options
        ]

    def filter(
        self,
        list_of_items: List[Dict[str, Any]],  # {"filename": filename, ["size": size]}
        verbose: bool = False,
        needed_for_rgb: Union[Callable, None] = None,
        is_rgb: Union[Callable, None] = None,
    ) -> List[str]:
        list_of_files: List[str] = []

        for item in list_of_items:
            if self.includes(
                item_filename=item["filename"],
                item_size=item.get("size", -1),
                verbose=verbose,
                needed_for_rgb=needed_for_rgb,
                is_rgb=is_rgb,
            ):
                list_of_files.append(item["filename"])

        return list_of_files

    def includes(
        self,
        item_filename: str,
        item_size: int = -1,
        verbose: bool = False,
        needed_for_rgb: Union[Callable, None] = None,
        is_rgb: Union[Callable, None] = None,
    ) -> bool:
        if self.all:
            return True

        if (
            self.metadata
            and item_size <= 10**6
            and not any(item_filename.endswith(suffix) for suffix in raster_suffix)
        ):
            return True

        if self.rgbx and (needed_for_rgb is not None) and needed_for_rgb(item_filename):
            return True

        if self.rgb and (is_rgb is not None) and is_rgb(item_filename):
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
