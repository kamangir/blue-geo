from enum import Enum, auto


class Area(Enum):
    EAST = auto()
    NORTH = auto()
    SOUTH = auto()
    WEST = auto()
    WORLD = auto()


class Source(Enum):
    LANDSAT_NRT = (
        auto(),
        "LANDSAT Near Real-Time, Real-Time and Ultra Real-Time [US/Canada only]",
    )
    MODIS_NRT = (
        auto(),
        "MODIS Near Real-Time, Real-Time and Ultra Real-Time",
    )
    MODIS_SP = (
        auto(),
        "(MODIS Standard Processing)",
    )
    VIIRS_NOAA20_NRT = (
        auto(),
        "VIIRS NOAA-20 Near Real-Time, Real-Time and Ultra Real-Time",
    )
    VIIRS_NOAA21_NRT = (
        auto(),
        "VIIRS NOAA-21 Near Real-Time, Real-Time and Ultra Real-Time",
    )
    VIIRS_SNPP_NRT = (
        auto(),
        "VIIRS Suomi-NPP Near Real-Time, Real-Time and Ultra Real-Time",
    )
    VIIRS_SNPP_SP = (
        auto(),
        "VIIRS Suomi-NPP Standard Processing",
    )

    def __init__(self, _, description):
        self.description = description
