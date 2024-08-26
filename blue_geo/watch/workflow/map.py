from blueness import module
from blue_geo import NAME
from blue_geo.watch.targets import Target
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def map_function(
    datacube_id: str,
    object_name: str,
) -> bool:
    success, target = Target.load(object_name)
    if not success:
        return success

    logger.info(
        "{}.map: {} @ {} -> {}".format(
            NAME,
            target,
            datacube_id,
            object_name,
        )
    )

    logger.info("🪄")

    return True
