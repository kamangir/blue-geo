from typing import Dict
from blue_geo.catalog.firms.area.enums import Area, Source
from datetime import datetime, timedelta

args: Dict[str, Dict] = {
    "area": {
        "default": Area.default().name,
        "help": "|".join(Area.values()),
    },
    "date": {
        "default": (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d"),
        "help": "yyyy-mm-dd",
    },
    "depth": {
        "type": int,
        "default": 1,
        "help": "1..10",
    },
    "source": {
        "default": Source.default().name,
        "help": "|".join(Source.values()),
    },
}
