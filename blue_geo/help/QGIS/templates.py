from typing import List

from blue_options.terminal import show_usage


def help_download(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "QGIS",
            "templates",
            "download",
        ],
        "download QGIS templates.",
        {
            "from: $BLUE_GEO_QGIS_TEMPLATES_OBJECT_NAME": "",
            "to: $BLUE_GEO_QGIS_PATH_TEMPLATES": "",
        },
        mono=mono,
    )


def help_upload(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "QGIS",
            "templates",
            "upload",
        ],
        "upload QGIS templates.",
        {
            "from: $BLUE_GEO_QGIS_PATH_TEMPLATES": "",
            "to: $BLUE_GEO_QGIS_TEMPLATES_OBJECT_NAME": "",
        },
        mono=mono,
    )


help_functions = {
    "download": help_download,
    "upload": help_upload,
}
