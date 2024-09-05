from typing import List, Union
from functools import reduce
from abcli import string
from blue_geo import REPO_NAME

url_prefix = "https://kamangir-public.s3.ca-central-1.amazonaws.com"


list_of_objects = {
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
        ],
    },
    "burning-man-2024": {},
    "Mount-Etna": {},
}


items: List[str] = []
for target_name in list_of_objects:
    items += [
        "## {}".format(target_name.replace("-", " ").title()),
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
        for object_name, description in list_of_objects[target_name].items()
    ]

    if list_of_objects[target_name]:
        last_object_name = list(list_of_objects[target_name].keys())[-1]
        items += [
            "",
            f"![image]({url_prefix}/{last_object_name}/{last_object_name}-2X.gif?raw=true&random={string.random_()})",
        ]

    items += [
        "",
        f"[details](./targets/{target_name}.md)",
        "",
    ]
