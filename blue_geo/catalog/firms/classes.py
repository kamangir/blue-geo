from blue_geo.catalog.generic import GenericCatalog


class FirmsCatalog(GenericCatalog):
    name = "firms"

    def __init__(self):
        super().__init__()
