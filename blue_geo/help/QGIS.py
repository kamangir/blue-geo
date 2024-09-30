from typing import List
import os

from blue_options.terminal import show_usage


def help_expressions_pull(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        "QGIS expressions pull",
        "pull QGIS expressions.",
        mono=mono,
    )


def help_expressions_push(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        "QGIS expressions push [push]",
        "push QGIS expressions.",
        {
            "QGIS: {}".format(
                os.getenv(
                    "abcli_QGIS_path_expressions",
                    "",
                )
            ): "",
            "github: {}".format(
                os.getenv(
                    "abcli_QGIS_path_expressions_git",
                    "",
                )
            ): "",
        },
        mono=mono,
    )


def help_seed(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        "QGIS seed [screen]",
        "seed 🌱 QGIS.",
        mono=mono,
    )


def help_server(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        "QGIS serve[r] [start]",
        "start QGIS server.",
        mono=mono,
    )


help_functions = {
    "expressions": {
        "push": help_expressions_push,
        "pull": help_expressions_pull,
    },
    "seed": help_seed,
    "server": help_server,
}
