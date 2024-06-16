import time
from typing import Union, List
import os
import random

if not QGIS_is_live:
    from log import log

blue_geo_QGIS_path_server = os.path.join(
    os.getenv("HOME", ""),
    "Downloads/QGIS/server",
)

os.makedirs(blue_geo_QGIS_path_server, exist_ok=True)


def seed(command: Union[str, List[str]]):
    if isinstance(command, list):
        command = " ".join(command)

    hash_id = "{}-{:05d}".format(
        time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())),
        random.randrange(100000),
    )

    with open(
        os.path.join(
            blue_geo_QGIS_path_server,
            f"{hash_id}.command",
        ),
        "w",
    ) as f:
        f.write(command)

    log(hash_id, command, icon="🌱")
