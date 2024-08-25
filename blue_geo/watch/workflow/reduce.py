from blueness import module
from blue_geo import NAME
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def reduce_function(object_name: str) -> bool:
    logger.info(f"{NAME}.reduce: {object_name}")

    logger.info("🪄")

    return True
