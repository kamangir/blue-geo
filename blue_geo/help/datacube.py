from typing import List

from blue_options.terminal import show_usage, xtra
from blue_options import env

from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo.datacube.modalities import options as modality_options


def ingest_options(mono: bool) -> str:
    return "".join(
        [
            xtra("~copy_template,dryrun,overwrite,", mono),
            "scope=<scope>",
            xtra(",upload", mono),
        ]
    )


def help_crop(
    tokens: List[str],
    mono: bool,
) -> str:
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


def help_generate(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono)

    args = [
        "[--modality <{}>]".format("|".join(modality_options)),
        "[--overwrite <1>]",
    ]

    return show_usage(
        [
            "@datacube generate",
            f"[{options}]",
            "[.|<datacube-id>]",
        ]
        + args,
        "generate datacube/<modality>.",
        mono=mono,
    )


def help_get(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "catalog|raw|template"

    return show_usage(
        [
            "@datacube get",
            f"[{options}]",
            "[.|<datacube-id>]",
        ],
        "get datacube properties.",
        mono=mono,
    )


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = ingest_options(mono)

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


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
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


help_functions = {
    "crop": help_crop,
    "generate": help_generate,
    "get": help_get,
    "ingest": help_ingest,
    "list": help_list,
}
