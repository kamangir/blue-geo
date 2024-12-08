import os

from blue_objects import file, README
from blue_objects.env import ABCLI_PUBLIC_PREFIX

from blue_geo import NAME, VERSION, ICON, REPO_NAME
from blue_geo.objects import special_objects


def build() -> bool:
    return all(
        README.build(
            path=os.path.join(
                file.path(__file__),
                f"md/{suffix}",
            ),
            macros=macros,
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
        )
        for suffix, macros, in [
            (
                f"{object_name}.md".replace("-", "_"),
                {
                    "--object-name--": [
                        "💾 [{}-{}]({}/{}-{}.tar.gz)".format(
                            object_name,
                            special_objects[object_name].version,
                            ABCLI_PUBLIC_PREFIX,
                            object_name,
                            special_objects[object_name].version,
                        ),
                    ],
                    "--urls--": sorted(
                        [
                            f" - {title}: {url}"
                            for title, url in special_objects[object_name].url.items()
                        ]
                    ),
                },
            )
            for object_name in [
                "global-power-plant-database",
            ]
        ]
    )
