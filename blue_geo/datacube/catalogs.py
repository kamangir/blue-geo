from typing import Tuple, List
from blue_geo.datacube.generic import GenericDatacube
from blue_geo.datacube.firms.area import FirmsAreaDatacube


list_of_datacube_classes: List[GenericDatacube] = [
    GenericDatacube,
    FirmsAreaDatacube,
]


def catalog_of(datacube_id: str) -> Tuple[bool, str]:
    for datacube_class in list_of_datacube_classes:
        success, _ = datacube_class.parse_datacube_id(datacube_id)
        if success:
            return True, datacube_class.catalog

    return False, "unknown-catalog"
