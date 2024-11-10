from typing import List

from blue_options.terminal import show_usage, xtra


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
            "@download",
            "[.|<object-name>]",
            f"[{open_options}]",
        ],
        "download object and its QGIS dependencies.",
        mono=mono,
    )


def help_expressions_pull(
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
            "from: $abcli_QGIS_path_expressions_git": "",
            "to: $abcli_QGIS_path_expressions": "",
        },
        mono=mono,
    )


def help_expressions_push(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "QGIS",
            "expressions",
            "push",
            "[push]",
        ],
        "push QGIS expressions.",
        {
            "from: $abcli_QGIS_path_expressions": "",
            "to: $abcli_QGIS_path_expressions_git": "",
        },
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
            "serve[r]",
            "[start]",
        ],
        "start QGIS server.",
        mono=mono,
    )


help_functions = {
    "download": help_download,
    "expressions": {
        "push": help_expressions_push,
        "pull": help_expressions_pull,
    },
    "seed": help_seed,
    "server": help_server,
}
