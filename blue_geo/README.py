import os

from blue_options import MARQUEE as default_MARQUEE
from blue_options.help.functions import get_help
from blue_objects import file, README
from blue_objects.env import ABCLI_PUBLIC_PREFIX

from blue_geo.catalog.README import build as build_catalog
from blue_geo.watch.README import items as watch_items, macros as watch_macros
from blue_geo.objects.README import build as build_objects
from blue_geo.watch.targets.README import build as build_targets
from blue_geo.help.functions import help_functions
from blue_geo import NAME, VERSION, ICON, REPO_NAME


features = {
    "Maxar Open Data": {
        "description": "catalog: [Maxar's Open Data program](https://www.maxar.com/open-data/)",
        "icon": "🧊",
        "thumbnail": "https://github.com/kamangir/assets/blob/main/blue-geo/MaxarOpenData.png?raw=true",
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data",
    },
    "copernicus": {
        "description": "catalog: [Copernicus Data Space Ecosystem - Europe's eyes on Earth](https://dataspace.copernicus.eu/)",
        "icon": "🧊",
        "thumbnail": "https://github.com/kamangir/assets/blob/main/blue-geo/copernicus.jpg?raw=true",
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/copernicus",
    },
    "SkyFox": {
        "description": "catalog: [Earth Data Store](https://earthdaily.github.io/EDA-Documentation/).",
        "icon": ICON,
        "thumbnail": "https://earthdaily.github.io/EDA-Documentation/Images/EarthDailyEDS.png",
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/SkyFox",
    },
    "EarthSearch": {
        "description": "catalog: [Earth Search by Element 84 (earth-search-aws)](https://stacindex.org/catalogs/earth-search#/).",
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/assets/blob/main/blue-geo/viewer-aws-element84-com.png?raw=true",
        "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/catalog/EarthSearch",
    },
    "firms-area": {
        "description": "catalog: Fire Information for Resource Management System ([FIRMS](https://firms.modaps.eosdis.nasa.gov)).",
        "icon": ICON,
        "thumbnail": "https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/datacube-firms_area.jpg",
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/firms",
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
    "geo-watch": {
        "description": "watch the planet's story unfold.",
        "icon": ICON,
        "thumbnail": f"{ABCLI_PUBLIC_PREFIX}/geo-watch-2024-09-06-Jasper-a/geo-watch-2024-09-06-Jasper-a-2X.gif",
        "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/watch",
    },
    "global-power-plant-database": {
        "description": "The Global Power Plant Database is a comprehensive, open source database of power plants around the world [datasets.wri.org](https://datasets.wri.org/datasets/global-power-plant-database).",
        "icon": ICON,
        "thumbnail": "https://github.com/kamangir/assets/blob/main/blue-geo/global_power_plant_database-cover.png?raw=true",
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/objects/md/global_power_plant_database.md",
    },
    "QGIS": {
        "description": "an AI terraform for [QGIS](https://www.qgis.org/).",
        "icon": ICON,
        "thumbnail": "https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/QGIS.jpg",
        "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/QGIS/README.md",
    },
    "catalog": {
        "description": "generalized STAC Catalogs.",
        "icon": ICON,
        "thumbnail": default_MARQUEE,
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog",
    },
    "datacube": {
        "description": "generalized STAC Items.",
        "icon": "🧊",
        "thumbnail": default_MARQUEE,
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/datacube",
    },
    "template": {
        "description": "",
        "icon": ICON,
        "thumbnail": default_MARQUEE,
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


def build() -> bool:
    return (
        all(
            README.build(
                items=items,
                cols=cols,
                path=os.path.join(file.path(__file__), suffix),
                macros=macros,
                ICON=ICON,
                NAME=NAME,
                VERSION=VERSION,
                REPO_NAME=REPO_NAME,
                help_function=lambda tokens: get_help(
                    tokens,
                    help_functions,
                    mono=True,
                ),
            )
            for suffix, items, cols, macros, in [
                ("..", items, 3, {}),
                ("catalog", [], -1, {}),
                ("datacube", [], -1, {}),
                ("watch", watch_items, -1, watch_macros),
                ("QGIS", [], -1, {}),
            ]
        )
        and build_catalog()
        and build_targets()
        and build_objects()
    )
