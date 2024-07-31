import os
from blueness import module
import abcli
from abcli import file
from abcli.file.functions import build_from_template
from abcli.plugins import markdown
from blue_geo import NAME, VERSION, ICON
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)

features = {
    "QGIS": {
        "description": "an AI terraform for [QGIS](https://www.qgis.org/).",
        "icon": ICON,
        "thumbnail": "https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/QGIS.jpg",
        "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/.abcli/QGIS/README.md",
    },
    "datacube": {
        "description": "a datacube for geospatial AI",
        "icon": "🧊",
        "thumbnail": "https://github.com/kamangir/assets/blob/main/blue-geo/datacube.png?raw=true",
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/.abcli/datacube",
    },
    "firms-area": {
        "description": "Fire Information for Resource Management System ([FIRMS](https://firms.modaps.eosdis.nasa.gov)) datacubes.",
        "icon": ICON,
        "thumbnail": "https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/datacube-firms_area.jpg",
        "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/.abcli/catalog/firms",
    },
    "ukraine-timemap": {
        "description": "`ingest` for the [Bellingcat](https://www.bellingcat.com/) [Civilian Harm in Ukraine TimeMap](https://github.com/bellingcat/ukraine-timemap) dataset, available through [this UI](https://ukraine.bellingcat.com/) and [this API](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json).",
        "icon": "🇺🇦",
        "thumbnail": "https://github.com/kamangir/assets/blob/main/nbs/ukraine-timemap/QGIS.png?raw=true",
        "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/.abcli/ukraine-timemap/README.md",
    },
    "vancouver-watching": {
        "description": "🌈 Vancouver watching with AI, last build: [🔗](https://kamangir-public.s3.ca-central-1.amazonaws.com/test_vancouver_watching_ingest/animation.gif).",
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


def build(filename: str = ""):
    if not filename:
        filename = os.path.join(file.path(__file__), "../README.md")

    logger.info(f"{NAME}.build: {filename}")

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

    table = markdown.generate_table(items, cols=2)

    signature = [
        "---",
        "built by [`{}`]({}), based on [`{}-{}`]({}).".format(
            abcli.fullname(),
            "https://github.com/kamangir/awesome-bash-cli",
            NAME,
            VERSION,
            "https://github.com/kamangir/blue-geo",
        ),
    ]

    return file.build_from_template(
        os.path.join(file.path(__file__), "./assets/README.md"),
        {
            "--table--": table,
            "--signature": signature,
        },
        filename,
    )
