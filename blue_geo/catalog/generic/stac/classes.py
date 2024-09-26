from typing import List, Tuple, Union
from pystac_client import Client

from blue_geo.catalog.generic.classes import GenericCatalog
from blue_geo.logger import logger


class STACCatalog(GenericCatalog):

    @classmethod
    def get_client(cls) -> Tuple[bool, Union[Client, None]]:
        try:
            # https://pystac-client.readthedocs.io/en/stable/
            client = Client.open(cls.url["api"])
        except Exception as e:
            logger.error(e)
            return False, None

        return True, client

    def get_list_of_collections(self) -> List[str]:
        success, client = self.get_client()
        if not success:
            return []

        return sorted([collection.id for collection in client.get_collections()])
