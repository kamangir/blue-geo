from typing import List
from pystac_client import Client  # https://pystac-client.readthedocs.io/en/stable/
from blue_geo.catalog.generic import GenericCatalog


class CopernicusCatalog(GenericCatalog):
    name = "copernicus"

    # https://documentation.dataspace.copernicus.eu/APIs/STAC.html
    url = "https://catalogue.dataspace.copernicus.eu/stac"

    def get_collection_names(self) -> List[str]:
        client = Client.open(self.url)
        return sorted([collection.id for collection in client.get_collections()])
