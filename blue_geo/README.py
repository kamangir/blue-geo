from abcli import file
from abcli.plugins.README import build as build_README
from blue_geo import NAME, VERSION, ICON, REPO_NAME


features = {
    "QGIS": {
        "description": "an AI terraform for [QGIS](https://www.qgis.org/).",
        "icon": ICON,
        "thumbnail": "https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/QGIS.jpg",
        "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/.abcli/QGIS/README.md",
    },
    "datacube": {
        "description": "a datacube for geospatial AI.",
        "icon": "🧊",
        "thumbnail": "https://github.com/kamangir/assets/blob/main/blue-geo/datacube.png?raw=true",
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/.abcli/datacube",
    },
    "firms-area": {
        "description": "catalog: Fire Information for Resource Management System ([FIRMS](https://firms.modaps.eosdis.nasa.gov)).",
        "icon": ICON,
        "thumbnail": "https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/datacube-firms_area.jpg",
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/.abcli/catalog/firms",
    },
    "ukraine-timemap": {
        "description": "catalog: [Bellingcat](https://www.bellingcat.com/) [Civilian Harm in Ukraine TimeMap](https://github.com/bellingcat/ukraine-timemap) dataset, available through [this UI](https://ukraine.bellingcat.com/) and [this API](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json).",
        "icon": "🇺🇦",
        "thumbnail": "https://github.com/kamangir/assets/blob/main/nbs/ukraine-timemap/QGIS.png?raw=true",
        "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/.abcli/catalog/ukraine_timemap",
    },
    "vancouver-watching": {
        "description": "catalog: Vancouver watching with AI, last build: [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_vancouver_watching_ingest/animation.gif).",
        "icon": "🌈",
        "thumbnail": "https://kamangir-public.s3.ca-central-1.amazonaws.com/test_vancouver_watching_ingest/animation.gif?raw=true",
        "url": "https://github.com/kamangir/Vancouver-Watching",
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
    return build_README(
        items=items,
        cols=2,
        path=file.path(__file__),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
