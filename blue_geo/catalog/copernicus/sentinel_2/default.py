from typing import Dict
from datetime import datetime, timedelta


args: Dict[str, Dict] = {
    "bbox": {
        "type": str,
        "default": "",
        "help": "<-122.88,51.73,-122.68,51.93>",
    },
    "datetime": {
        "default": "{}/{}".format(
            (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
            datetime.now().strftime("%Y-%m-%d"),
        ),
        "help": "<2024-07-30/2024-08-09>",
    },
    "lat": {
        "type": float,
        "default": 51.83,
        "help": "<51.83>",
    },
    "lon": {
        "type": float,
        "default": -122.78,
        "help": "<-122.78>",
    },
    "count": {
        "type": int,
        "default": -1,
        "help": "<10>, -1: all",
    },
    "radius": {
        "type": float,
        "default": 0.1,
        "help": "<0.1>",
    },
}
