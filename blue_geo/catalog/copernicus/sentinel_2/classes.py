from typing import Any, Tuple, Dict
from blueness import module
from blue_geo import NAME
from abcli.plugins.metadata import post_to_object
from blue_geo.catalog.copernicus.classes import CopernicusCatalog
from blue_geo.catalog.generic.datacube import GenericDatacube
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


class CopernicusSentinel2Datacube(GenericDatacube):
    name = "sentinel_2"
    catalog = CopernicusCatalog()
    QGIS_template = "unknown-template"

    @staticmethod
    def query(object_name: str, **kwargs) -> bool:
        return post_to_object(
            object_name,
            "datacube_id",
            [],  # TODO
        )
