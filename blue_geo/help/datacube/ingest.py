from typing import List

from blue_options.terminal import show_usage, xtra

from blue_geo.catalog.generic.generic.scope import DatacubeScope


def ingest_options(mono: bool) -> str:
    return "".join(
        [
            xtra("~copy_template,dryrun,overwrite,", mono),
            "scope=<scope>,upload",
        ]
    )


scope_details = {
    f"scope: {DatacubeScope.help}": [
        "all: ALL files.",
        "metadata (default): any < 1 MB.",
        "raster: all raster.",
        "rgb: rgb.",
        "rgbx: rgb and what is needed to build rgb.",
        "<suffix>: any *<suffix>.",
    ]
}


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@datacube",
            "ingest",
            f"[{ingest_options(mono)}]",
            "[.|<datacube-id>]",
            "[<args>]",
        ],
        "ingest <datacube-id>/<scope>.",
        scope_details,
        mono=mono,
    )
