from typing import List

from blue_options.terminal import show_usage, xtra


def help_label(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,~QGIS,~rasterize,", mono=mono),
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
