from typing import List

from blue_options.terminal import show_usage


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "catalogs"

    args = [
        "[--count 1]",
        "[--delim ,]",
        "[--log 0]",
    ]

    usage_1 = show_usage(
        [
            "@catalog list",
            f"[{options}]",
        ]
        + args,
        "list catalogs.",
        mono=mono,
    )

    # ----

    options = "collections|datacubes==datacube_classes"

    args = ["[--catalog <catalog>]"] + args

    usage_2 = show_usage(
        [
            "@catalog list",
            f"[{options}]",
        ]
        + args,
        f"list {options} in <catalog>.",
        mono=mono,
    )

    # ----

    return "\n".join(
        [
            usage_1,
            usage_2,
        ]
    )
