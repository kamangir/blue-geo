from typing import Any, Tuple, Dict
from . import NAME
from blue_geo.logger import logger


class GenericDatacube:
    catalog = "generic"

    def __init__(self):
        pass

    @property
    def datacube_id(self) -> str:
        return f"datacube-{self.catalog}"

    @property
    def description(self) -> str:
        return "{}.{}@{}[{}]:".format(
            NAME,
            self.__class__.__name__,
            self.catalog,
            self.datacube_id,
        )

    def ingest(self, object_name: str) -> Tuple[bool, Any]:
        logger.info(
            "{}.{} -> {}".format(
                NAME,
                self.__class__.__name__,
                object_name,
            )
        )
        return True, None

    @classmethod
    def parse_datacube_id(cls, datacube_id: str) -> Tuple[
        bool,
        Dict[str, Any],
    ]:
        # datacube-<catalog>-<args>
        pieces = datacube_id.split("-") + ["", ""]

        return (
            pieces[0] == "datacube" and pieces[1] == cls.catalog,
            {},
        )
