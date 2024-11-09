import os
from glob import glob

from blue_objects.env import ABCLI_OBJECT_ROOT
from blue_objects import file, path

from blue_geo import VERSION


def generate_seed() -> str:
    path = os.path.join(file.path(__file__), "console")

    apps_path = os.getenv(
        "BLUE_GEO_QGIS_APPS_PATH",
        os.path.join(path, "apps"),
    )

    list_of_files = (
        [
            os.path.join(path, f"{module}.py")
            for module in [
                "log",
                "project",
                "layer",
                "application",
                "seed",
                "QGIS",
                "alias",
            ]
        ]
        + sorted(glob(f"{apps_path}/*.py"))
        + [os.path.join(path, "main.py")]
    )

    seed = "; ".join(
        [
            f'ABCLI_OBJECT_ROOT="{ABCLI_OBJECT_ROOT}"',
            f'BLUE_GEO_VERSION="{VERSION}"',
        ]
        + [f'exec(Path("{filename}").read_text())' for filename in list_of_files]
    )

    return seed
