from typing import List
import os

from blue_options import string
from blue_objects import file
from blue_objects.env import ABCLI_PUBLIC_PREFIX

from blue_geo import REPO_NAME


list_of_targets = {
    "chilcotin-river-landslide": {
        "objects": {
            "test_blue_geo_watch_v4-chilcotin-river-landslide-test": [
                f"[![bashtest](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml)"
            ],
            "geo-watch-2024-08-31-chilcotin-c": [
                "L1C and L2A mixed",
                "`2024-07-30/2024-08-09`",
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-199-11f9b5497ef0)",
            ],
            "geo-watch-2024-09-01-chilcotin-a": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-201-d64e9bb3716b)",
            ],
            "geo-watch-2024-09-01-chilcotin-c": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-202-d59ba811398b)",
                "[on reddit](https://www.reddit.com/r/bash/comments/1f9cvyx/a_bash_python_tool_to_watch_a_target_in_satellite/).",
            ],
        },
    },
    "burning-man-2024": {
        "objects": {
            "geo-watch-2024-09-04-burning-man-2024-a": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-205-c272a95ce266)",
            ]
        },
    },
    "Mount-Etna": {
        "objects": {
            "geo-watch-2024-09-04-Mount-Etna-a": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-205-c272a95ce266)",
            ]
        },
    },
    "Fagradalsfjall": {
        "objects": {
            "geo-watch-2024-09-04-Fagradalsfjall-a": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-206-f7996520dc15)",
            ]
        },
    },
    "Jasper": {
        "objects": {
            "geo-watch-2024-09-06-Jasper-a": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-208-7063fca1423b)",
            ]
        },
    },
    "Leonardo": {
        "objects": {
            "test_blue_geo_watch_v4-Leonardo-test": [
                f"[![bashtest](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml)"
            ],
            "geo-watch-2024-09-30-Leonardo-g": [
                "[dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-237-99db71023445)",
            ],
        },
        "thumbnail": {
            "scale": 4,
        },
    },
    "bellingcat-2024–09–27-nagorno-karabakh": {
        "objects": {
            "bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b": [
                "[background](https://www.bellingcat.com/news/mena/2024/09/27/nagorno-karabakh-satellite-imagery-shows-city-wide-ransacking/)",
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-241-3e25857747a5)",
            ],
            "bellingcat-2024-09-27-nagorno-karabakh-b": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-244-a5f9b7959748)",
            ],
            "bellingcat-2024-09-27-nagorno-karabakh-6X-a": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-245-18f6d15e5fbd)",
            ],
        },
        "thumnail": {
            "index": 1,
        },
    },
}

targets_path = file.path(__file__)

items: List[str] = []
for target_name in list_of_targets:
    list_of_objects = list_of_targets[target_name]["objects"]

    target_README = f"./targets/{target_name}.md"

    target_title = target_name.replace("-", " ").title()

    items += [
        (
            f"## [{target_title}]({target_README})"
            if file.exists(os.path.join(targets_path, target_README))
            else f"## {target_title}"
        ),
    ]

    items += [
        "- {}.".format(
            ", ".join(
                [
                    f"[`{object_name}`]({ABCLI_PUBLIC_PREFIX}/{object_name}.tar.gz)",
                    f"[gif]({ABCLI_PUBLIC_PREFIX}/{object_name}/{object_name}.gif)",
                ]
                + description
            )
        )
        for object_name, description in list_of_objects.items()
    ]

    if list_of_objects:
        thumbnail_info = list_of_targets[target_name].get("showcase", {})
        thumbnail_index = thumbnail_info.get("index", -1)
        thumbnail_scale = thumbnail_info.get("scale", 2)

        last_object_name = list(list_of_objects.keys())[thumbnail_index]
        items += [
            "",
            f"![image]({ABCLI_PUBLIC_PREFIX}/{last_object_name}/{last_object_name}-{thumbnail_scale}X.gif?raw=true&random={string.random()})",
        ]

    items += [""]
