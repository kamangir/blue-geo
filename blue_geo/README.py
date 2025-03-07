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


items = README.Items(
    [
        {
            "name": "Maxar Open Data",
            "description": "catalog: [Maxar's Open Data program](https://www.maxar.com/open-data/)",
            "marquee": "https://github.com/kamangir/assets/blob/main/blue-geo/MaxarOpenData.png?raw=true",
            "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/maxar_open_data",
        },
        {
            "name": "copernicus",
            "description": "catalog: [Copernicus Data Space Ecosystem - Europe's eyes on Earth](https://dataspace.copernicus.eu/)",
            "marquee": "https://github.com/kamangir/assets/blob/main/blue-geo/copernicus.jpg?raw=true",
            "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/copernicus",
        },
        {
            "name": "SkyFox",
            "description": "catalog: [Earth Data Store](https://earthdaily.github.io/EDA-Documentation/).",
            "marquee": "https://earthdaily.github.io/EDA-Documentation/Images/EarthDailyEDS.png",
            "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/SkyFox",
        },
        {
            "name": "EarthSearch",
            "description": "catalog: [Earth Search by Element 84 (earth-search-aws)](https://stacindex.org/catalogs/earth-search#/).",
            "marquee": "https://github.com/kamangir/assets/blob/main/blue-geo/viewer-aws-element84-com.png?raw=true",
            "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/catalog/EarthSearch",
        },
        {
            "name": "firms-area",
            "description": "catalog: Fire Information for Resource Management System ([FIRMS](https://firms.modaps.eosdis.nasa.gov)).",
            "marquee": "https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/datacube-firms_area.jpg",
            "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog/firms",
        },
        {
            "name": "ukraine-timemap",
            "description": "catalog: [Bellingcat](https://www.bellingcat.com/) [Civilian Harm in Ukraine TimeMap](https://github.com/bellingcat/ukraine-timemap) dataset, available through [this UI](https://ukraine.bellingcat.com/) and [this API](https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json).",
            "marquee": "https://github.com/kamangir/assets/blob/main/nbs/ukraine-timemap/QGIS.png?raw=true",
            "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/catalog/ukraine_timemap",
        },
        {
            "name": "vancouver-watching",
            "description": f"catalog: Vancouver watching with AI, last build: [🔗]({ABCLI_PUBLIC_PREFIX}/test_vancouver_watching_ingest/animation.gif).",
            "marquee": f"{ABCLI_PUBLIC_PREFIX}/2024-01-06-20-39-46-73614/2024-01-06-20-39-46-73614-2X.gif?raw=true",
            "url": "https://github.com/kamangir/Vancouver-Watching",
        },
        {
            "name": "geo-watch",
            "description": "watch the planet's story unfold.",
            "marquee": f"{ABCLI_PUBLIC_PREFIX}/geo-watch-2024-09-06-Jasper-a/geo-watch-2024-09-06-Jasper-a-2X.gif",
            "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/watch",
        },
        {
            "name": "global-power-plant-database",
            "description": "The Global Power Plant Database is a comprehensive, open source database of power plants around the world [datasets.wri.org](https://datasets.wri.org/datasets/global-power-plant-database).",
            "marquee": "https://github.com/kamangir/assets/blob/main/blue-geo/global_power_plant_database-cover.png?raw=true",
            "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/objects/md/global_power_plant_database.md",
        },
        {
            "name": "QGIS",
            "description": "an AI terraform for [QGIS](https://www.qgis.org/).",
            "marquee": "https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/QGIS.jpg",
            "url": "https://github.com/kamangir/blue-geo/blob/main/blue_geo/QGIS/README.md",
        },
        {
            "name": "catalog",
            "description": "generalized STAC Catalogs.",
            "marquee": default_MARQUEE,
            "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/catalog",
        },
        {
            "name": "datacube",
            "description": "generalized STAC Items.",
            "marquee": default_MARQUEE,
            "url": "https://github.com/kamangir/blue-geo/tree/main/blue_geo/datacube",
        },
    ]
)


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
