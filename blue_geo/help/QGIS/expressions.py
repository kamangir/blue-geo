from typing import List

from blue_options.terminal import show_usage


def help_pull(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "QGIS",
            "expressions",
            "pull",
        ],
        "pull QGIS expressions.",
        {
            "from: $BLUE_GEO_QGIS_PATH_EXPRESSIONS_GIT": "",
            "to: $BLUE_GEO_QGIS_PATH_EXPRESSIONS": "",
        },
        mono=mono,
    )


def help_push(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "QGIS",
            "expressions",
            "push",
        ],
        "push QGIS expressions.",
        {
            "from: $BLUE_GEO_QGIS_PATH_EXPRESSIONS": "",
            "to: $BLUE_GEO_QGIS_PATH_EXPRESSIONS_GIT": "",
        },
        mono=mono,
    )


help_functions = {
    "push": help_push,
    "pull": help_pull,
}
