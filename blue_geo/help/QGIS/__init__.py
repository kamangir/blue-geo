from typing import List

from blue_options.terminal import show_usage, xtra

from blue_geo.help.QGIS.expressions import help_functions as help_expressions
from blue_geo.help.QGIS.templates import help_functions as help_templates


def help_download(
    tokens: List[str],
    mono: bool,
) -> str:
    open_options = "".join(
        [
            "open",
            xtra(",~QGIS", mono=mono),
        ]
    )

    return show_usage(
        [
            "QGIS",
            "download",
            "[.|<object-name>]",
            f"[{open_options}]",
        ],
        "download object and its QGIS dependencies.",
        mono=mono,
    )


def help_seed(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "QGIS",
            "seed",
            "[screen]",
        ],
        "seed 🌱 QGIS.",
        mono=mono,
    )


def help_server(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "QGIS",
            "server",
            "[start]",
        ],
        "start QGIS server.",
        mono=mono,
    )


def help_upload(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "QGIS",
            "upload",
            "[.|<object-name>]",
        ],
        "upload object and its QGIS dependencies.",
        mono=mono,
    )


help_functions = {
    "download": help_download,
    "expressions": help_expressions,
    "seed": help_seed,
    "server": help_server,
    "templates": help_templates,
    "upload": help_upload,
}
