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

    if tokens[0] == "get":
        what = "is_STAC|url:<...>|url_args|list_of_args"
        args = ["[--catalog <catalog>]"]
        return show_usage(
            [
                "@catalog get",
                f"[{what}]",
            ]
            + args,
            "get catalog properties.",
            mono=mono,
        )

    if tokens[0] == "list":
        options = "catalogs"
        args = [
            "[--count 1]",
            "[--delim ,]",
            "[--log 0]",
        ]
        usage_1 = show_usage(
            [
                "@catalog list",
                f"[{options}]",
            ]
            + args,
            "list catalogs.",
            mono=mono,
        )

        options = "collections|datacubes==datacube_classes"
        args = ["[--catalog <catalog>]"] + args
        usage_2 = show_usage(
            [
                "@catalog list",
                f"[{options}]",
            ]
            + args,
            f"list {options} in <catalog>.",
            mono=mono,
        )

        return "\n".join([usage_1, usage_2])

    return ""
