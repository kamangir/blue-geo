import time
from typing import Union, List
import os
import random

if not QGIS_is_live:
    from logger import Q_log

blue_geo_QGIS_path_server = os.path.join(
    os.getenv("HOME", ""),
    "Downloads/QGIS/server",
)

os.makedirs(blue_geo_QGIS_path_server, exist_ok=True)


def Q_seed(
    command: Union[str, List[str]],
    dryrun: bool = False,
):
    if isinstance(command, list):
        command = " ".join(command)

    command_name = "{}-{:05d}".format(
        time.strftime("QGIS-command-%Y-%m-%d-%H-%M-%S", time.localtime(time.time())),
        random.randrange(100000),
    )

    if not dryrun:
        with open(
            os.path.join(
                blue_geo_QGIS_path_server,
                f"{command_name}.command",
            ),
            "w",
        ) as f:
            f.write(command)

    Q_log(command_name, command, icon="🌱")
