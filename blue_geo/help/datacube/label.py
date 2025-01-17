from typing import List

from blue_options.terminal import show_usage, xtra


def help_label(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~download,dryrun,~QGIS,~rasterize,~sync,", mono=mono),
            "upload",
        ]
    )

    return show_usage(
        [
            "@datacube",
            "label",
            f"[{options}]",
            "[.|<datacube-id>]",
        ],
        "label <datacube-id>.",
        mono=mono,
    )
