import os

from blue_options.help.functions import get_help
from blue_objects import file, README

from blue_geo import NAME, VERSION, ICON, REPO_NAME
from blue_geo.watch.targets import jasper
from blue_geo.help.functions import help_functions
from blue_geo.watch.targets.target_list import TargetList


def build() -> bool:
    target_list = TargetList(download=True)

    return all(
        README.build(
            items=items,
            cols=cols,
            path=os.path.join(
                file.path(__file__),
                f"md/{suffix}",
            ),
            macros=macros,
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
            help_function=lambda tokens: get_help(
                tokens,
                help_functions,
                mono=True,
            ),
        )
        for suffix, items, cols, macros, in [
            (
                f"{target_name}.md",
                jasper.items if target_name == "Jasper" else [],
                len(jasper.list_of_dates) if target_name == "Jasper" else 3,
                {
                    "--footer--": [
                        "---",
                        "",
                        "used by: {}.".format(
                            ", ".join(
                                sorted(
                                    [
                                        "[`@geo watch`](../../)",
                                    ]
                                )
                            )
                        ),
                    ],
                    "--urls--": target_list.get(target_name).urls_as_str(),
                },
            )
            for target_name in [
                "Fagradalsfjall",
                "Hurricane-Idalia-2023",
                "Jasper",
                "Leonardo",
                "Mount-Etna",
                "burning-man-2024",
                "chilcotin-river-landslide",
            ]
        ]
    )
