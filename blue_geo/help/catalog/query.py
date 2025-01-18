from typing import List

from blue_options.terminal import show_usage, xtra

from blue_geo.help.datacube.ingest import ingest_options
from blue_geo.catalog.functions import get_datacube_class_in_catalog
from blue_geo.catalog.default import as_list_of_args
from blue_geo.catalog.classes import list_of_catalogs
from blue_geo.catalog.functions import get_list_of_datacube_classes
from blue_geo.help.datacube import ingest_options as datacube_ingest_options
from blue_geo.help.datacube import scope_details


def help_query(
    tokens: List[str],
    mono: bool,
) -> str:
    if not tokens:
        return "\n".join(
            [
                help_query([token], mono)
                for token in ["ingest", "read"] + list_of_catalogs
            ]
        )

    if tokens[0] == "ingest":
        return help_query_ingest(tokens[1:], mono=mono)

    if tokens[0] == "read":
        return help_query_read(tokens[1:], mono=mono)

    catalog_name = tokens[0]

    if len(tokens) < 2:
        return "\n".join(
            [
                help_query([catalog_name, collection_name], mono)
                for collection_name in [
                    datacube_class.name
                    for datacube_class in get_list_of_datacube_classes(
                        catalog_class=catalog_name
                    )
                ]
            ]
        )

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
            f"[ingest,{ingest_options(mono)}]",
            "[-|<object-name>]",
        ]
        + args,
        f"{catalog_name}/{datacube_class_name} -query-> <object-name>.",
        {
            "scope: @datacube ingest help.": "",
        },
        mono=mono,
    )


def help_query_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("download", mono=mono)

    return show_usage(
        [
            "@catalog",
            "query",
            "ingest",
            f"[{options}]",
            "[.|<query-object-name>]",
            f"[{datacube_ingest_options(mono)}]",
        ],
        "ingest the datacubes in the query.",
        scope_details,
        mono=mono,
    )


def help_query_read(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "all,len"

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
            "[.|<query-object-name>]",
        ]
        + args,
        "read the query.",
        mono=mono,
    )
