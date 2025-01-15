from typing import List

from blue_options.terminal import show_usage, xtra


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun,~upload", mono=mono)

    args = [
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@maxar",
            "ingest",
            f"[{options}]",
            "[.|<datacube-id>]",
        ]
        + args,
        "ingest <datacube-id>.",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "collections",
            xtra(",source=open_data", mono=mono),
        ]
    )

    return show_usage(
        [
            "@maxar",
            "list",
            f"[{options}]",
        ],
        "list collections.",
        mono=mono,
    )


help_functions = {
    "ingest": help_ingest,
    "list": help_list,
}
