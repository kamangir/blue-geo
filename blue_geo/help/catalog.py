from typing import List

from blue_options.terminal import show_usage

from blue_geo.catalog import get_catalog
from blue_geo.help.datacube import ingest_options
from blue_geo.catalog.functions import get_datacube_class_in_catalog
from blue_geo.catalog.default import as_list_of_args
from blue_geo.logger import logger


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    catalog_name = tokens[0]
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


def help_get(
    tokens: List[str],
    mono: bool,
) -> str:
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


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
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


def help_query(
    tokens: List[str],
    mono: bool,
) -> str:
    if len(tokens) < 2:
        logger.error(f"2 tokens expected: {tokens}")
        return ""

    catalog_name = tokens[0]

    if catalog_name == "read":
        return help_query_read(tokens[1:], mono=mono)

    datacube_class_name = tokens[1]
    datacube_class = get_datacube_class_in_catalog(
        catalog_name,
        datacube_class_name,
    )
    args = as_list_of_args(datacube_class.query_args)
    options = f"dryrun,{datacube_class_name},select,upload"

    return show_usage(
        [
            f"@catalog query {catalog_name}",
            f"[{options}]",
            f"ingest,{ingest_options}",
            "[-|<object-name>]",
        ]
        + args,
        f"{catalog_name}/{datacube_class_name} -query-> <object-name>.",
        {
            "scope: @datacube ingest help.": "",
        },
        mono=mono,
    )


def help_query_read(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "all,download,len"
    args = [
        "[--count <count>]",
        "[--delim <delim>]",
        "[--offset <offset>]",
        "[--prefix <prefix>]",
        "[--suffix <suffix>]",
        "[--contains <contains>]",
        "[--notcontains <not-contains>]",
    ]

    return show_usage(
        [
            "@catalog query read",
            f"[{options}]",
            "[.|<object-name>]",
        ]
        + args,
        "read query results in <object-name>.",
        mono=mono,
    )


help_functions = {
    "browse": help_browse,
    "get": help_get,
    "list": help_list,
    "query": help_query,
}
