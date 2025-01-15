from typing import List

from blue_options.terminal import show_usage, xtra


def help_log(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~download,dryrun,", mono=mono),
            "filename=<filename.tif>,upload",
        ]
    )

    args = [
        "[--log <0>]",
        "[--verbose <0>]",
        "[--header <some-text>]",
        "[--footer <some-text>]",
    ]

    return show_usage(
        [
            "@geo",
            "log",
            f"[{options}]",
            "[.|<object-name>]",
        ]
        + args,
        "log <object-name>/<filename.tif>.",
        mono=mono,
    )
