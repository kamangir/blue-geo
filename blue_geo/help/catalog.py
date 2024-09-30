from typing import List

from blue_options.terminal import show_usage
from blue_options import env

from blue_geo.catalog import get_catalog
from blue_geo.catalog.generic.generic.scope import DatacubeScope


def get(
    tokens: List[str],
    mono: bool,
) -> str:
    if tokens[0] == "browse":
        catalog_name = tokens[1]
        catalog = get_catalog(catalog_name)

        return show_usage(
            [
                "@catalog browse",
                catalog_name,
                "|".join(catalog.url.keys()),
            ],
            f"browse {catalog_name}.",
            mono=mono,
        )

    return ""
