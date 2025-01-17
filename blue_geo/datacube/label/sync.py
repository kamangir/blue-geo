from blueness import module

from blue_geo import NAME
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


def sync_the_label(
    datacube_id: str,
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.sync_the_label({datacube_id})")

    logger.info("🪄")

    return True
