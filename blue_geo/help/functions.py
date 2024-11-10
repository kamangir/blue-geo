from abcli.help.generic import help_functions as generic_help_functions

from blue_geo import ALIAS
from blue_geo.help.catalog import help_functions as help_catalog
from blue_geo.help.datacube import help_functions as help_datacube
from blue_geo.help.gdal import help_functions as help_gdal
from blue_geo.help.QGIS import help_functions as help_QGIS
from blue_geo.help.watch import help_functions as help_watch

help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "catalog": help_catalog,
        "datacube": help_datacube,
        "gdal": help_gdal,
        "QGIS": help_QGIS,
        "watch": help_watch,
    }
)
