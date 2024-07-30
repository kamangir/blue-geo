from typing import Any, Tuple, Dict
from blueness import module
from blue_geo import NAME
from abcli.plugins.metadata import post_to_object
from blue_geo.catalog.generic.classes import GenericCatalog, VoidCatalog
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


class GenericDatacube:
    name = "generic"
    catalog = GenericCatalog()
    QGIS_template = "unknown-template"

    def __init__(self, datacube_id: str = ""):
        pass

    @property
    def datacube_id(self) -> str:
        return f"datacube-{self.catalog.name}"

    @property
    def description(self) -> str:
        return "{}.{}@{}[{}]:".format(
            NAME,
            self.__class__.__name__,
            self.catalog.name,
            self.datacube_id,
        )

    def ingest(self, object_name: str) -> Tuple[bool, Any]:
        logger.info("{} -> {}".format(self.description, object_name))
        return True, None

    @classmethod
    def parse_datacube_id(cls, datacube_id: str) -> Tuple[
        bool,
        Dict[str, Any],
    ]:
        # datacube-<catalog-name>-<args>
        segments = datacube_id.split("-") + ["", ""]

        return (
            segments[0] == "datacube" and segments[1] == cls.catalog.name,
            {},
        )

    @staticmethod
    def query(object_name: str) -> bool:
        return post_to_object(object_name, "datacube_id", [])


class VoidDatacube(GenericDatacube):
    name = "void"
    catalog = VoidCatalog()
