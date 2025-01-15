from typing import List, Dict

from blue_geo.catalog.generic import GenericCatalog
from blue_geo.catalog.maxar_open_data.client import MaxarOpenDataClient


class MaxarOpenDataCatalog(GenericCatalog):
    name: str = "maxar_open_data"

    url: Dict[str, str] = {
        "home": "https://www.maxar.com/open-data",
    }

    def __init__(self):
        self.client = MaxarOpenDataClient()

        self.list_of_collections: List[str] = []

    def get_list_of_collections(
        self,
        use_cache: bool = True,
    ) -> List[str]:
        if not use_cache:
            self.list_of_collections = []

        if not self.list_of_collections:
            self.list_of_collections = self.client.get_list_of_collections()

        return self.list_of_collections
