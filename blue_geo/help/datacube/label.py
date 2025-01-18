from typing import List

from blue_options.terminal import show_usage, xtra


def options(mono: bool) -> str:
    return "".join(
        [
            xtra("~download,dryrun,~QGIS,~rasterize,~sync,", mono=mono),
            "upload",
        ]
    )


def help_label(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@datacube",
            "label",
            f"[{options(mono=mono)}]",
            "[.|<datacube-id>]",
        ],
        "label <datacube-id>.",
        mono=mono,
    )
