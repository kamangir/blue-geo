import os
from glob import glob

from blue_objects.env import ABCLI_OBJECT_ROOT
from blue_objects import file, path

from blue_geo import VERSION


def generate_seed() -> str:
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
                "console/log",
                "console/project",
                "console/layer",
                "console/fileio",
                "console/application",
                "console/seed",
                "console/QGIS",
                "console/alias",
            ]
        ]
        + sorted(glob(f"{apps_path}/*.py"))
        + [os.path.join(path, "console/main.py")]
    )

    seed = "; ".join(
        [
            f'ABCLI_OBJECT_ROOT="{ABCLI_OBJECT_ROOT}"',
            f'BLUE_GEO_VERSION="{VERSION}"',
        ]
        + [f'exec(Path("{filename}").read_text())' for filename in list_of_files]
    )

    return seed
