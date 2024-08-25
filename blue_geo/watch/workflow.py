from blueness import module
from blue_geo import NAME
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


def generate_workflow(
    query_object_name: str,
    job_name: str,
    object_name: str,
    processing_options: str,
) -> bool:
    logger.info(
        "{}.generate_workflow: {}: -[ {} @ {}]-> {}".format(
            query_object_name,
            processing_options,
            job_name,
            object_name,
        )
    )

    logger.info("🪄")

    return True
