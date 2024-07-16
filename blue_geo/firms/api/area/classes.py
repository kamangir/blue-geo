from . import NAME
from .enums import Area, Source
from blue_geo.logger import logger


class APIRequest:
    def __init__(
        self,
        source: Source = Source.MODIS_NRT,
        area: Area = Area.WORLD,
    ):
        self.area: Area = area
        self.source: Source = source

    def as_str(self) -> str:
        return "{}.{}, area:{}, source: {} ({})".format(
            NAME,
            self.__class__.__name__,
            self.area.name.lower(),
            self.source.name,
            self.source.description,
        )

    def get_url(self) -> str:
        return ""
