from blueness import module
from blue_geo.watch.targets import Target
from blue_geo.logger import logger
from blue_geo import NAME

NAME = module.name(__file__, NAME)


def generate_target_shape(
    object_name: str,
    target: Target,
) -> bool:
    logger.info(
        "{}.generate_target_shape: {} -> {})".format(
            NAME,
            target,
            object_name,
        )
    )

    logger.info("🪄")

    # save in objects.path_of("target/shape.shp",object_name)

    return True
