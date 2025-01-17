import os
from typing import List
from glob import glob

from blue_objects.env import ABCLI_OBJECT_ROOT
from blue_objects import file, path

from blue_geo import VERSION

default_init_script: List[str] = [
    "QGIS.test",
    "QGIS.help",
]


def generate_seed(
    init_script: List[str] = default_init_script,
) -> str:
    path = file.path(__file__)

    apps_path = os.getenv(
        "BLUE_GEO_QGIS_APPS_PATH",
        os.path.join(path, "console/apps"),
    )

    list_of_files = (
        [
            os.path.join(path, f"{module}.py")
            for module in [
                "dependency",
                "console/logger",
                "console/project",
                "console/layer",
                "console/file",
                "console/file_load",
                "console/file_save",
                "console/graphics",
                "console/objects",
                "console/path",
                "console/string",
                "console/application",
                "console/seed",
                "console/help",
                "console/QGIS",
            ]
        ]
        + sorted(glob(f"{apps_path}/*.py"))
        + sorted(glob(os.path.join(path, "console/tests/*.py")))
        + [
            os.path.join(path, f"console/{module}.py")
            for module in [
                "main",
                "testing",
            ]
        ]
    )

    seed: List[str] = (
        [
            f'ABCLI_OBJECT_ROOT="{ABCLI_OBJECT_ROOT}"',
            f'BLUE_GEO_VERSION="{VERSION}"',
        ]
        + [f'exec(Path("{filename}").read_text())' for filename in list_of_files]
        + init_script
    )

    return "; ".join(seed)
