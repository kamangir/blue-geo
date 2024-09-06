from typing import List, Union
from functools import reduce
from abcli import string
from blue_geo import REPO_NAME

url_prefix = "https://kamangir-public.s3.ca-central-1.amazonaws.com"


list_of_targets = {
    "chilcotin-river-landslide": {
        "test_blue_geo_watch": [
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
    "burning-man-2024": {
        "geo-watch-2024-09-04-burning-man-2024-a": [
            "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-205-c272a95ce266)",
        ]
    },
    "Mount-Etna": {
        "geo-watch-2024-09-04-Mount-Etna-a": [
            "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-205-c272a95ce266)",
        ]
    },
    "Fagradalsfjall": {
        "geo-watch-2024-09-04-Fagradalsfjall-a": [
            "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-206-f7996520dc15)",
        ]
    },
}


items: List[str] = []
for target_name, list_of_objects in list_of_targets.items():
    items += [
        "## [{}]({})".format(
            target_name.replace("-", " ").title(),
            f"./targets/{target_name}.md",
        ),
    ]

    items += [
        "- {}.".format(
            ", ".join(
                [
                    f"[`{object_name}`]({url_prefix}/{object_name}.tar.gz)",
                    f"[gif]({url_prefix}/{object_name}/{object_name}.gif)",
                ]
                + description
            )
        )
        for object_name, description in list_of_objects.items()
    ]

    if list_of_objects:
        last_object_name = list(list_of_objects.keys())[-1]
        items += [
            "",
            f"![image]({url_prefix}/{last_object_name}/{last_object_name}-2X.gif?raw=true&random={string.random_()})",
        ]

    items += [""]
