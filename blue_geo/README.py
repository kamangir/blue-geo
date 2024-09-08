from abcli import file
import os
from abcli.plugins.README import build as build_README
from blue_objects.env import ABCLI_PUBLIC_PREFIX
from blue_geo.watch.targets.jasper import (
    items as jasper_items,
    list_of_dates as jasper_dates,
)
from blue_geo.watch.README import items as watch_items
from blue_geo import NAME, VERSION, ICON, REPO_NAME


features = {
    "copernicus": {
        "description": "catalog: [Copernicus Data Space Ecosystem - Europe's eyes on Earth](https://dataspace.copernicus.eu/)",
        "icon": "🧊",
        "thumbnail": "https://github.com/kamangir/assets/blob/main/blue-geo/copernicus.jpg?raw=true",
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/copernicus",
    },
    "firms-area": {
        "description": "catalog: Fire Information for Resource Management System ([FIRMS](https://firms.modaps.eosdis.nasa.gov)).",
        "icon": ICON,
        "thumbnail": "https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/datacube-firms_area.jpg",
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/firms",
    },
    "EarthSearch": {
        "description": "catalog: [Earth Search by Element 84 (earth-search-aws)](https://stacindex.org/catalogs/earth-search#/).",
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/assets/blob/main/blue-geo/viewer-aws-element84-com.png?raw=true",
        "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/catalog/EarthSearch",
    },
    "ukraine-timemap": {
        "description": "catalog: [Bellingcat](https://www.bellingcat.com/) [Civilian Harm in Ukraine TimeMap](https://github.com/bellingcat/ukraine-timemap) dataset, available through [this UI](https://ukraine.bellingcat.com/) and [this API](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json).",
        "icon": "🇺🇦",
        "thumbnail": "https://github.com/kamangir/assets/blob/main/nbs/ukraine-timemap/QGIS.png?raw=true",
        "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/catalog/ukraine_timemap",
    },
    "vancouver-watching": {
        "description": f"catalog: Vancouver watching with AI, last build: [🔗]({ABCLI_PUBLIC_PREFIX}/test_vancouver_watching_ingest/animation.gif).",
        "icon": "🌈",
        "thumbnail": f"{ABCLI_PUBLIC_PREFIX}/2024-01-06-20-39-46-73614/2024-01-06-20-39-46-73614-2X.gif?raw=true",
        "url": "https://github.com/kamangir/Vancouver-Watching",
    },
    "QGIS": {
        "description": "an AI terraform for [QGIS](https://www.qgis.org/).",
        "icon": ICON,
        "thumbnail": "https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/QGIS.jpg",
        "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/QGIS/README.md",
    },
    "geo-watch": {
        "description": "watching targets through `@geo`.",
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/assets/blob/main/blue-geo/blue-geo-watch.png?raw=true",
        "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/watch",
    },
    "template": {
        "description": "",
        "icon": "",
        "thumbnail": "",
        "url": "",
    },
}


items = [
    "{}[`{}`]({}) [![image]({})]({}) {}".format(
        details["icon"],
        feature,
        details["url"],
        details["thumbnail"],
        details["url"],
        details["description"],
    )
    for feature, details in features.items()
    if feature != "template"
]


def build():
    return all(
        build_README(
            items=items,
            cols=cols,
            path=os.path.join(file.path(__file__), suffix),
            ICON=ICON,
            NAME=NAME,
            VERSION=VERSION,
            REPO_NAME=REPO_NAME,
        )
        for suffix, items, cols, in [
            ("..", items, 3),
            ("catalog/copernicus", [], 3),
            ("catalog/EarthSearch", [], 3),
            ("watch", watch_items, -1),
            ("watch/targets/Jasper.md", jasper_items, len(jasper_dates)),
        ]
    )
