from typing import List

from blue_options.terminal import show_usage


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
