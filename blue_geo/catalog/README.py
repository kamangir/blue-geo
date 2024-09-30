import os
from typing import List

from blue_objects import file, README

from blue_geo.catalog import get_catalog
from blue_geo.help.functions import get as get_help
from blue_geo import NAME, VERSION, ICON, REPO_NAME


def build() -> bool:
    return all(
        README.build(
            items=[],
            cols=3,
            path=os.path.join(file.path(__file__), suffix),
            macros=macros,
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
            help_function=lambda tokens: get_help(
                tokens,
                mono=True,
            ),
        )
        for suffix, macros, in [
            (catalog, {"--urls--": get_catalog(catalog).urls_as_str()})
            for catalog in [
                "copernicus",
                "EarthSearch",
                "SkyFox",
                "firms",
                "ukraine_timemap",
            ]
        ]
    )
