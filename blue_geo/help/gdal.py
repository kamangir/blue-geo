from typing import List

from blue_options.terminal import show_usage


def help_get_crs(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@gdal",
            "get_crs",
            "<filename>",
        ],
        "get <filename> crs.",
        mono=mono,
    )


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@gdal",
            "install",
        ],
        "install gdal.",
        mono=mono,
    )


def help_version(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@gdal",
            "version",
        ],
        "show gdal version.",
        mono=mono,
    )


help_functions = {
    "get_crs": help_get_crs,
    "install": help_install,
    "version": help_version,
}
