from typing import List
from pystac_client import Client  # https://pystac-client.readthedocs.io/en/stable/
from blue_geo.catalog.generic import GenericCatalog


class CopernicusCatalog(GenericCatalog):
    name = "copernicus"

    url = {
        "": "https://dataspace.copernicus.eu/",
        # https://documentation.dataspace.copernicus.eu/APIs/STAC.html
        "api": "https://catalogue.dataspace.copernicus.eu/stac",
        "aws_access": "https://documentation.dataspace.copernicus.eu/APIs/S3.html",
        "doc": "https://documentation.dataspace.copernicus.eu/APIs/STAC.html",
        "docs": "https://documentation.dataspace.copernicus.eu/APIs/STAC.html",
    }

    def get_list_of_collections(self) -> List[str]:
        client = Client.open(self.url["api"])
        return sorted([collection.id for collection in client.get_collections()])
