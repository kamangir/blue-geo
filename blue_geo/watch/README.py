from typing import List, Dict
import os

from blue_options import string
from blue_objects import file
from blue_geo.watch.targets.target_list import TargetList
from blue_geo.watch.targets.bellingcat_2024_09_27_nagorno_karabakh import (
    README as bellingcat_2024_09_27_nagorno_karabakh,
)
from blue_geo.watch.targets.burning_man_2024 import README as burning_man_2024
from blue_geo.watch.targets.Cache_Creek import README as Cache_Creek
from blue_geo.watch.targets.chilcotin_river_landslide import (
    README as chilcotin_river_landslide,
)
from blue_geo.watch.targets.DrugSuperLab import README as DrugSuperLab
from blue_geo.watch.targets.elkhema import README as elkhema
from blue_geo.watch.targets.jasper import README as jasper
from blue_geo.watch.targets.Fagradalsfjall import README as Fagradalsfjall
from blue_geo.watch.targets.Leonardo import README as Leonardo
from blue_geo.watch.targets.Mount_Etna import README as Mount_Etna
from blue_geo.watch.targets.Palisades import README as Palisades
from blue_geo.watch.targets.Sheerness import README as Sheerness
from blue_geo.watch.targets.Silver_Peak import README as Silver_Peak
from blue_objects.env import ABCLI_PUBLIC_PREFIX


list_of_targets = {
    "DrugSuperLab": DrugSuperLab,
    "chilcotin-river-landslide": chilcotin_river_landslide,
    "burning-man-2024": burning_man_2024,
    "Mount-Etna": Mount_Etna,
    "Palisades": Palisades,
    "Fagradalsfjall": Fagradalsfjall,
    "Jasper": jasper,
    "Leonardo": Leonardo,
    "bellingcat-2024-09-27-nagorno-karabakh": bellingcat_2024_09_27_nagorno_karabakh,
    "elkhema": elkhema,
    "Cache-Creek": Cache_Creek,
    "Sheerness": Sheerness,
    "Silver-Peak": Silver_Peak,
}

targets_path = file.path(__file__)

items: List[str] = []
for target_name in sorted(list_of_targets.keys()):
    target_info = list_of_targets[target_name]

    list_of_objects = target_info["objects"]
    assert isinstance(list_of_objects, dict)

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

    if list_of_objects:
        thumbnail_info = target_info.get("thumbnail", {})
        assert isinstance(thumbnail_info, dict)

        thumbnail_index = thumbnail_info.get("index", -1)

        thumbnail_scale = thumbnail_info.get("scale", 2)
        thumbnail_scale_str = f"-{thumbnail_scale}X" if thumbnail_scale != 1 else ""

        thumbnail_object_name = list(list_of_objects.keys())[thumbnail_index]

        thumbnail_url = (
            f"{ABCLI_PUBLIC_PREFIX}/{thumbnail_object_name}/{thumbnail_object_name}.gif"
        )

        thumbnail_scale_url = f"{ABCLI_PUBLIC_PREFIX}/{thumbnail_object_name}/{thumbnail_object_name}{thumbnail_scale_str}.gif"

        items += [
            "",
            "<details>",
            "<summary>🌐</summary>",
            "",
            f"[![image]({thumbnail_scale_url}?raw=true&random={string.random()})]({thumbnail_url})",
            "",
            "</details>",
            "",
        ]

    items += target_list.get(
        target_info.get(
            "target_name",
            target_name,
        )
    ).urls_as_str()

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
