from typing import List

from blue_options.terminal import show_usage, xtra

from blue_geo.datacube.modalities import options as modality_options


def help_generate(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("dryrun", mono)

    args = [
        "[--modality <{}>]".format("|".join(modality_options)),
        "[--overwrite <1>]",
    ]

    return show_usage(
        [
            "@datacube generate",
            f"[{options}]",
            "[.|<datacube-id>]",
        ]
        + args,
        "generate datacube/<modality>.",
        mono=mono,
    )
