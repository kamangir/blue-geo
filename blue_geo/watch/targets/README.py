import os
from typing import List

from blue_objects import file, README
from blue_geo import NAME, VERSION, ICON, REPO_NAME
from blue_geo.watch.targets import jasper
from blue_geo.watch.targets.classes import TargetList, Target


def build() -> bool:
    target_list = TargetList(os.path.join(file.path(__file__), "../targets.yaml"))

    return all(
        README.build(
            items=items,
            cols=cols,
            path=os.path.join(file.path(__file__), suffix),
            macros=macros,
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
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
                        "details: [targets.yaml](../targets.yaml).",
                        "",
                        "used by: {}.".format(
                            ", ".join(
                                sorted(
                                    [
                                        "[`@geo watch`](../)",
                                    ]
                                )
                            )
                        ),
                    ],
                    "--urls--": urls_as_str(target_list.targets[target_name]),
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


def urls_as_str(target: Target) -> List[str]:
    return sorted(
        [
            " - [{}]({}){}".format(
                title,
                url.split(",", 1)[0],
                (
                    ": {}".format(
                        target.lat_and_lon
                        if title == "Google Map"
                        else url.split(",", 1)[1].strip()
                    )
                    if "," in url or title == "Google Map"
                    else ""
                ),
            )
            for title, url in target.urls.items()
        ]
    )
