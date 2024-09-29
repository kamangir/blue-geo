from typing import List
import os

from blue_options.terminal import show_usage


def get(
    tokens: List[str],
    mono: bool,
) -> str:
    if tokens[0] == "expressions":
        if tokens[1] == "pull":
            return show_usage(
                "QGIS expressions pull",
                "pull QGIS expressions.",
                mono=mono,
            )

        if tokens[1] == "push":
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

    if tokens[0] == "seed":
        return show_usage(
            "QGIS seed [screen]",
            "seed 🌱 QGIS.",
            mono=mono,
        )

    if tokens[0] == "server":
        return show_usage(
            "QGIS serve[r] [start]",
            "start QGIS server.",
            mono=mono,
        )

    return ""
