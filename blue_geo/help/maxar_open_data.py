from typing import List

from blue_options.terminal import show_usage, xtra

list_of_events = [
    "Maui-Hawaii-fires-Aug-23",
    "...",
]


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~download,dryrun,", mono=mono),
            "event=<event>",
            xtra(",~gdal,~rm,source=open_data,~upload", mono=mono),
        ]
    )

    args = [
        "[--verbose 1]",
    ]

    return show_usage(
        [
            "@maxar",
            "ingest",
            f"[{options}]",
            "[-|<dataset-object-name>]",
        ]
        + args,
        "ingest <event> -> <dataset-object-name>.",
        {
            "event: {}".format(" | ".join(list_of_events)): [],
        },
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "events",
            xtra(",source=open_data", mono=mono),
        ]
    )

    usage_1 = show_usage(
        [
            "@maxar",
            "list",
            f"[{options}]",
        ],
        "list events.",
        mono=mono,
    )

    # ---

    options = "".join(
        [
            "event=<event>",
            xtra(",source=open_data", mono=mono),
        ]
    )

    usage_2 = show_usage(
        [
            "@maxar",
            "list",
            f"[{options}]",
            "<suffix>",
        ],
        "list <event> acquisitions.",
        mono=mono,
    )

    # ---

    return "\n".join(
        [
            usage_1,
            usage_2,
        ]
    )


help_functions = {
    "ingest": help_ingest,
    "list": help_list,
}
