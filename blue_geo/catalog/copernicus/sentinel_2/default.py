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
        "default": 0,
        "help": "<51.83>",
    },
    "lon": {
        "type": float,
        "default": 0,
        "help": "<-122.78>",
    },
    "limit": {
        "type": int,
        "default": 10,
        "help": "<10>",
    },
    "radius": {
        "type": float,
        "default": 0.1,
        "help": "<0.1>",
    },
}
