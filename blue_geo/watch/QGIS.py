from blueness import module
from blue_geo.watch.targets import Target
from blue_geo.logger import logger
from blue_geo import NAME

NAME = module.name(__file__, NAME)


def generate_marker(
    object_name: str,
    target: Target,
) -> bool:
    logger.info(
        "{}.generate_marker: {} -> {})".format(
            NAME,
            target,
            object_name,
        )
    )

    logger.info("🪄")

    return True
