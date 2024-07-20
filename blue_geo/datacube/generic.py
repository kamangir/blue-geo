from typing import Any, Tuple
from . import NAME
from blue_geo.logger import logger


class GenericDatacube:
    type = "generic"

    def __init__(self):
        pass

    @property
    def datacube_id(self) -> str:
        return f"blue-geo-{self.type}"

    @property
    def description(self) -> str:
        return "{}.{}: {}".format(
            NAME,
            self.__class__.__name__,
            self.type,
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
