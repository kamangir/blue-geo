from typing import List, Dict
import os

from blue_options import string
from blue_objects import file
from blue_geo.watch.targets.target_list import TargetList
from blue_objects.env import ABCLI_PUBLIC_PREFIX

from blue_geo import REPO_NAME


list_of_targets = {
    "DrugSuperLab": {
        "objects": {
            "geo-watch-DrugSuperLab-2024-11-19-13954": [],
        },
        "thumbnail": {
            "scale": 4,
        },
    },
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
            ],
            "geo-watch-2024-09-01-chilcotin-a": [],
            "geo-watch-2024-09-01-chilcotin-c": [
                "[on reddit](https://www.reddit.com/r/bash/comments/1f9cvyx/a_bash_python_tool_to_watch_a_target_in_satellite/).",
            ],
            "geo-watch-Chilcotin-2024-11-03": [],
        },
        "thumbnail": {
            "scale": 4,
        },
    },
    "burning-man-2024": {
        "objects": {"geo-watch-2024-09-04-burning-man-2024-a": []},
    },
    "Mount-Etna": {
        "objects": {"geo-watch-2024-09-04-Mount-Etna-a": []},
    },
    "Fagradalsfjall": {
        "objects": {"geo-watch-2024-09-04-Fagradalsfjall-a": []},
    },
    "Jasper": {
        "objects": {
            "geo-watch-2024-09-06-Jasper-a": [],
            "geo-watch-Jasper-2024-11-03": [],
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
            "geo-watch-2024-09-30-Leonardo-g": [],
            "geo-watch-Leonardo-2024-10-05-a": [],
            "geo-watch-Leonardo-2024-10-06-a": [],
            "geo-watch-2024-10-27-16-17-36-12059": [],
        },
        "thumbnail": {
            "scale": 4,
        },
    },
    "bellingcat-2024-09-27-nagorno-karabakh": {
        "objects": {
            "bellingcat-2024-09-27-nagorno-karabakh-2024-10-01-c-b": [],
            "bellingcat-2024-09-27-nagorno-karabakh-b": [],
            "bellingcat-2024-09-27-nagorno-karabakh-6X-a": [],
            "geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-05-b": [],
            "geo-watch-bellingcat-2024-09-27-nagorno-karabakh-6X-2024-10-06-a": [],
        },
        "thumbnail": {
            "scale": 4,
        },
    },
    "elkhema": {
        "objects": {"geo-watch-elkhema-2024-2024-10-05-a-b": []},
        "thumbnail": {
            "scale": 4,
        },
        "title": "elkhema ⛺️",
    },
    "Cache-Creek": {
        "objects": {
            "geo-watch-Cache-Creek-2024-10-06-a": [],
            "geo-watch-Cache-Creek-2x-wider-2024-10-06-a": [],
            "geo-watch-Cache-Creek-2024-11-05": [],
            "geo-watch-Cache-Creek-2x-wider-2024-11-05": [],
        },
        "thumbnail": {
            "scale": 4,
        },
    },
    "Silver-Peak": {
        "objects": {
            "geo-watch-Silver-Peak-2024-10-12-a": [],
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
