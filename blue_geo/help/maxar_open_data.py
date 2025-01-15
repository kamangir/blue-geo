from typing import List

from blue_options.terminal import show_usage, xtra


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "collections",
            xtra(",source=open_data", mono=mono),
        ]
    )

    return show_usage(
        [
            "@maxar",
            "list",
            f"[{options}]",
        ],
        "list collections.",
        mono=mono,
    )


help_functions = {
    "list": help_list,
}
