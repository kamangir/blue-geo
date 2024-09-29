from typing import List

from blue_options.terminal import show_usage


def get(
    tokens: List[str],
    mono: bool,
) -> str:
    if tokens[0] == "version":
        return show_usage(
            "@gdal version",
            "show gdal version.",
            mono=mono,
        )

    return ""
