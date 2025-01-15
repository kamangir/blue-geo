from typing import List, Dict

from blue_geo.catalog.generic import GenericCatalog
from blue_geo.maxar_open_data import MaxarOpenDataClient


class MaxarOpenDataCatalog(GenericCatalog):
    name: str = "maxar_open_data"

    url: Dict[str, str] = {
        "home": "https://www.maxar.com/open-data",
    }

    def __init__(self):
        self.client = MaxarOpenDataClient()

    def get_list_of_collections(self) -> List[str]:
        return self.client.get_list_of_collections()
