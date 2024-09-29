from typing import List

from blue_options.terminal import show_usage
from blue_options import env

from blue_geo.catalog.generic.generic.scope import DatacubeScope


ingest_options = (
    f"{env.EOP}~copy_template,dryrun,overwrite,upload,{env.LIGHTBLUE}scope=<scope>"
)


def get(
    tokens: List[str],
    mono: bool,
) -> str:
    if tokens[0] == "crop":
        options = "download,dryrun,suffix=<suffix>"
        return show_usage(
            [
                "@datacube crop",
                f"[{options}]",
                "[..|<object-name>]",
                "[.|<datacube-id>]",
            ],
            "crop <datacube-id> by <object-name>/target/shape.geojson -> <datacube-id>-DERIVED-crop-<suffix>.",
            mono=mono,
        )

    if tokens[0] == "get":
        options = "catalog|template"

        return show_usage(
            [
                "@datacube get",
                f"[{options}]",
                "[.|<datacube-id>]",
            ],
            "get datacube properties.",
            mono=mono,
        )

    if tokens[0] == "ingest":
        options = ingest_options

        return show_usage(
            [
                "@datacube ingest",
                f"[{options}]",
                "[.|<datacube-id>]",
                "[<args>]",
            ],
            "ingest <datacube-id>/<scope>.",
            {
                f"scope={DatacubeScope.help}": [
                    "all: ALL files.",
                    "metadata (default): any < 1 MB.",
                    "raster: all raster.",
                    "rgb: rgb.",
                    "rgbx: rgb and what is needed to build rgb.",
                    "<suffix>: any *<suffix>.",
                ]
            },
            mono=mono,
        )

    if tokens[0] == "list":
        args = [
            "[--count 1]",
            "[--delim +]",
            "[--exists 1]",
            "[--log 0]",
            f"[--scope {DatacubeScope.help}]",
        ]

        return show_usage(
            [
                "@datacube list",
                "[.|<datacube-id>]",
            ]
            + args,
            "list datacube files.",
            mono=mono,
        )

    return ""
