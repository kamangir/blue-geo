from typing import List
from blue_geo.logger import logger


class GenericCatalog:
    name: str = "generic"

    def __init__(self):
        pass

    # list of collections that are not implemented as datacubes.
    def get_collection_names(self) -> List[str]:
        return []


class VoidCatalog(GenericCatalog):
    name = "void"
