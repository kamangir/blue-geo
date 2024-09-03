from typing import List
from pystac_client import Client
from blue_geo.catalog.generic.classes import GenericCatalog


class STACCatalog(GenericCatalog):

    def get_list_of_collections(self) -> List[str]:
        # https://pystac-client.readthedocs.io/en/stable/
        client = Client.open(self.url["api"])

        return sorted([collection.id for collection in client.get_collections()])
