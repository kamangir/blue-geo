from typing import List

from blue_options.terminal import show_usage


def help_version(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        "@gdal version",
        "show gdal version.",
        mono=mono,
    )


help_functions = {
    "version": help_version,
}
