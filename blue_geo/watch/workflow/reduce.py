from blueness import module
from blue_geo import NAME
from blue_geo.watch.targets import Target
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def reduce_function(
    query_object_name: str,
    suffix: str,
    object_name: str,
) -> bool:
    success, target = Target.load(object_name)
    if not success:
        return success

    logger.info(
        "{}.reduce {}/{} @ {} -> {}".format(
            NAME,
            query_object_name,
            suffix,
            target,
            object_name,
        )
    )

    logger.info("🪄")

    return True
