from typing import List

from blue_options.terminal import show_usage, xtra

from blue_geo.objects import special_objects


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "publish,upload",
            xtra(",version=<v1>", mono=mono),
        ]
    )

    args = [
        "[--overwrite 1]",
    ]

    return show_usage(
        [
            "@geo",
            "ingest",
            f"[{options}]",
            "<object-name>",
        ]
        + args,
        "ingest <object-name>.",
        {
            "object-name: {}".format(" | ".join(special_objects.keys())): [],
        },
        mono=mono,
    )
