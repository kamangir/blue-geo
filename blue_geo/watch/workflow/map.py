from blueness import module
from blue_geo import NAME
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def map_function(
    datacube_id: str,
    object_name: str,
) -> bool:
    logger.info(f"{NAME}.map: {datacube_id} -> {object_name}")

    logger.info("🪄")

    return True
