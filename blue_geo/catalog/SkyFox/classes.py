from blue_geo.catalog.generic.stac.classes import STACCatalog


class SkyFoxCatalog(STACCatalog):
    name = "skyfox"

    url = {
        "account": "https://console.earthdaily.com/account",
        "doc": "https://earthdaily.github.io/EDA-Documentation/",
        "platform": "https://console.earthdaily.com/platform",
        "signin": "https://console.earthdaily.com/mosaics/signin",
    }
