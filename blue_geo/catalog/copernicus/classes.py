from blue_geo.catalog.generic.stac.classes import STACCatalog


class CopernicusCatalog(STACCatalog):
    name = "copernicus"

    url = {
        "home": "https://dataspace.copernicus.eu/",
        "api": "https://catalogue.dataspace.copernicus.eu/stac",
        "aws-access": "https://documentation.dataspace.copernicus.eu/APIs/S3.html",
        "docs": "https://documentation.dataspace.copernicus.eu/APIs/STAC.html",
    }
