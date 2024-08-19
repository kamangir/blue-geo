from typing import List
from blue_geo.logger import logger


class GenericCatalog:
    name: str = "generic"

    def __init__(self):
        pass

    def get_list_of_collections(self) -> List[str]:
        return []


class VoidCatalog(GenericCatalog):
    name = "void"
