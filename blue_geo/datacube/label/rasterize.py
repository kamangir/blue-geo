from blueness import module

from blue_geo import NAME
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


def rasterize_the_label(
    datacube_id: str,
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.rasterize_the_label({datacube_id})")

    logger.info("🪄")

    return True
