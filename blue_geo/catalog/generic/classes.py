from typing import List
from blue_geo.logger import logger


class GenericCatalog:
    name = "generic"

    def __init__(self):
        pass


class VoidCatalog(GenericCatalog):
    name = "void"
