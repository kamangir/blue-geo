from datetime import datetime, timedelta
from . import NAME
from .enums import Area, Source
from blue_geo import env
from blue_geo.logger import logger


class APIRequest:
    def __init__(
        self,
        source: Source = Source.MODIS_NRT,
        area: Area = Area.WORLD,
        date: str = "",
        day_range: int = 1,
        log: bool = True,
    ):
        self.prefix = "https://firms.modaps.eosdis.nasa.gov"
        self.map_key = env.FIRMS_MAP_KEY

        self.area: Area = area
        self.source: Source = source

        assert day_range >= 1
        assert day_range <= 10
        self.day_range: int = day_range

        self.date: str = (
            date if date else (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
        )

        if log:
            logger.info(self.as_str())

    def as_str(self) -> str:
        return "{}.{}, area:{}, source: {} ({})".format(
            NAME,
            self.__class__.__name__,
            self.area.name.lower(),
            self.source.name,
            self.source.description,
        )

    def url(self, html: bool = False) -> str:
        return "{}/api/area/{}/{}/{}/{}/{}/{}".format(
            self.prefix,
            "html" if html else "csv",
            self.map_key,
            self.source.name,
            self.area.name.lower(),
            self.day_range,
            self.date,
        )
