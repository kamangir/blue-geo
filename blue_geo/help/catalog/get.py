from typing import List

from blue_options.terminal import show_usage


def help_get(
    tokens: List[str],
    mono: bool,
) -> str:
    what = "is_STAC|url:<...>|url_args|list_of_args"
    args = ["[--catalog <catalog>]"]
    return show_usage(
        [
            "@catalog get",
            f"[{what}]",
        ]
        + args,
        "get catalog properties.",
        mono=mono,
    )
