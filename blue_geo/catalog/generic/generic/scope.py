from typing import List


class DatacubeScope:
    special_options = ["all", "metadata", "quick", "raster"]

    help = "|".join(special_options + ["<.jp2+.tif+.tiff>"])

    default = "metadata"

    def __init__(self, what: str):
        list_of_what = what.split("+")

        self.all = "all" in list_of_what

        self.metadata = "metadata" in list_of_what

        self.quick = "quick" in list_of_what

        self.raster = "raster" in list_of_what

        self.suffix = [
            item for item in list_of_what if item not in self.special_options
        ]
