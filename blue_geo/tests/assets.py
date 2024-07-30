from blue_geo.catalog.generic import GenericDatacube, VoidDatacube
from blue_geo.catalog.firms.area import FirmsAreaDatacube
from blue_geo import env


datacubes = {
    "void": VoidDatacube,
    "void-void-void-void-void-void-void-void": VoidDatacube,
    #
    "datacube-void-void-void": VoidDatacube,
    "datacube-generic": GenericDatacube,
    #
    "datacube-firms_void-void-void-void-void": VoidDatacube,
    "datacube-firms_area-void-void-void-void": VoidDatacube,
    "datacube-firms-area-void-void-void-void": VoidDatacube,
    "datacube-firms-area-world-void-2024-07-20-1": VoidDatacube,
    "datacube-firms-area-void-MODIS_NRT-2024-07-20-1": VoidDatacube,
    env.BLUE_GEO_TEST_DATACUBE_FIRMS_AREA: FirmsAreaDatacube,
}
