from typing import List, Dict
import os

from blue_options import string
from blue_objects import file
from blue_geo.watch.targets.target_list import TargetList
from blue_objects.env import ABCLI_PUBLIC_PREFIX

from blue_geo import REPO_NAME


list_of_targets = {
    "chilcotin-river-landslide": {
        "objects": {
            #            "test_blue_geo_watch_v4-diff-chilcotin-river-landslide-test": [
            #                f"[![bashtest](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml)"
            #            ],
            "test_blue_geo_watch_v4-modality-chilcotin-river-landslide-test": [
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
            "geo-watch-Chilcotin-2024-11-03": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-307-b4ed600efc16)",
            ],
        },
        "thumbnail": {
            "scale": 4,
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
            ],
            "geo-watch-Jasper-2024-11-03": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-307-b4ed600efc16)",
            ],
        },
    },
    "Leonardo": {
        "objects": {
            "test_blue_geo_watch_v4-diff-Leonardo-test": [
                f"[![bashtest](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml)"
            ],
            "test_blue_geo_watch_v4-modality-Leonardo-test": [
                f"[![bashtest](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/{REPO_NAME}/actions/workflows/bashtest.yml)"
            ],
            "geo-watch-2024-09-30-Leonardo-g": [
                "[dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-237-99db71023445)",
            ],
            "geo-watch-Leonardo-2024-10-05-a": [
                "[dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-249-44ba1dcd2321)",
            ],
            "geo-watch-Leonardo-2024-10-06-a": [
                "[dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-255-1f2a8f1ccef5)",
            ],
            "geo-watch-2024-10-27-16-17-36-12059": [
                "[dev note](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-294-1bba1bdc3c16)",
            ],
        },
        "thumbnail": {
            "scale": 4,
        },
    },
    "bellingcat-2024-09-27-nagorno-karabakh": {
        "objects": {
            "bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-241-3e25857747a5)",
            ],
            "bellingcat-2024-09-27-nagorno-karabakh-b": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-244-a5f9b7959748)",
            ],
            "bellingcat-2024-09-27-nagorno-karabakh-6X-a": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-245-18f6d15e5fbd)",
            ],
            "geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b": [
                "[dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-250-847d3d5f0d6e)",
            ],
            "geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a": [
                "[dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-255-1f2a8f1ccef5)",
            ],
        },
        "thumbnail": {
            "scale": 4,
        },
    },
    "elkhema": {
        "objects": {
            "geo-watch-elkhema-2024-2024-10-05-a-b": [
                "[dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-251-a68fab7f52b8)",
            ]
        },
        "thumbnail": {
            "scale": 4,
        },
        "title": "elkhema ⛺️",
    },
    "Cache-Creek": {
        "objects": {
            "geo-watch-Cache-Creek-2024-10-06-a": [
                "[dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-253-8f12ef5bd8fc)",
            ],
            "geo-watch-Cache-Creek-2x-wider-2024-10-06-a": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-256-c1b564c9f89e)"
            ],
            "geo-watch-Cache-Creek-2024-11-05": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-308-2d1de0179db1)",
            ],
            "geo-watch-Cache-Creek-2x-wider-2024-11-05": [
                "[dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-conversations-with-ai-309-ee21dd00730c)",
            ],
        },
        "thumbnail": {
            "scale": 4,
        },
    },
    "Silver-Peak": {
        "objects": {
            "geo-watch-Silver-Peak-2024-10-12-a": [
                "[dev notes](https://medium.com/@arash-kamangir/%EF%B8%8F-conversations-with-ai-267-8720fd3460d0)",
            ],
        },
        "thumbnail": {
            "scale": 4,
        },
    },
}

targets_path = file.path(__file__)

items: List[str] = []
for target_name in sorted(list_of_targets.keys()):
    target_info = list_of_targets[target_name]

    list_of_objects = target_info["objects"]

    target_README = f"./targets/md/{target_name}.md"

    target_title = "`{}`".format(target_info.get("title", target_name))

    items += [
        (
            f"## [{target_title}]({target_README})"
            if file.exists(os.path.join(targets_path, target_README))
            else f"## {target_title}"
        ),
    ]

    target_list = TargetList()
    items += target_list.get(target_name).urls_as_str()

    if list_of_objects:
        thumbnail_info = target_info.get("thumbnail", {})

        thumbnail_index = thumbnail_info.get("index", -1)

        thumbnail_scale = thumbnail_info.get("scale", 2)
        thumbnail_scale_str = f"-{thumbnail_scale}X" if thumbnail_scale != 1 else ""

        thumbnail_object_name = list(list_of_objects.keys())[thumbnail_index]
        items += [
            "",
            f"![image]({ABCLI_PUBLIC_PREFIX}/{thumbnail_object_name}/{thumbnail_object_name}{thumbnail_scale_str}.gif?raw=true&random={string.random()})",
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

    items += [""]

object_name = "geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b"
macros: Dict[str, str] = {
    "--scale-note--": [
        "ℹ️ suffix published gif urls with `-2X` and `-4X` for different scales. example: {}.".format(
            ", ".join(
                [
                    "[{}X]({}/{}/{}{}.gif)".format(
                        scale,
                        ABCLI_PUBLIC_PREFIX,
                        object_name,
                        object_name,
                        "" if scale == 1 else f"-{scale}X",
                    )
                    for scale in [1, 2, 4]
                ]
            )
        )
    ]
}
