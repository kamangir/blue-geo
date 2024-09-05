from abcli import file
import os
from abcli.plugins.README import build as build_README
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
        "description": "catalog: Vancouver watching with AI, last build: [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_vancouver_watching_ingest/animation.gif).",
        "icon": "🌈",
        "thumbnail": "https://kamangir-public.s3.ca-central-1.amazonaws.com/test_vancouver_watching_ingest/animation.gif?raw=true",
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
        for items, cols, suffix in zip(
            [[], [], watch_items, items],
            [3, 3, -1, 3],
            ["catalog/copernicus", "catalog/EarthSearch", "watch", ".."],
        )
    )
