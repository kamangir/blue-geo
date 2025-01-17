from typing import List

from blue_options.terminal import show_usage

from blue_geo.help.datacube.ingest import scope_details


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--count 1]",
        "[--delim +]",
        "[--exists 1]",
        "[--log 0]",
        "[--scope <scope>]",
    ]

    return show_usage(
        [
            "@datacube list",
            "[.|<datacube-id>]",
        ]
        + args,
        "list datacube files.",
        scope_details,
        mono=mono,
    )
