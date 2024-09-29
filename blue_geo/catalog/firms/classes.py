from blueness import module
from blue_geo import NAME
from blue_geo.catalog.generic import GenericCatalog
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


class FirmsCatalog(GenericCatalog):
    name = "firms"

    url = {
        "home": "https://firms.modaps.eosdis.nasa.gov/",
        "area": "https://firms.modaps.eosdis.nasa.gov/api/area/",
        "map-key": "https://firms.modaps.eosdis.nasa.gov/api/map_key/",
    }
