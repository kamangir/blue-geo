from typing import List
from blueness import module
from blue_geo import NAME
from blue_geo.catalog.copernicus.sentinel_2.classes import CopernicusSentinel2Datacube
from blue_geo.watch.targets import Target
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


def generate_workflow(
    job_name: str,
    object_name: str,
    frame_count: int,
    radius_degree: float,
    target: Target,
    process_options: str,
    dryrun: bool = False,
) -> bool:
    logger.info(
        "{}.generate_workflow: {} @ {} X @ {} deg : {} -{}-> {}".format(
            NAME,
            target,
            frame_count,
            radius_degree,
            process_options,
            job_name,
            object_name,
        )
    )

    success = CopernicusSentinel2Datacube.query(
        object_name=f"{job_name}-query",
        bbox=[
            target.lon - radius_degree,
            target.lat - radius_degree,
            target.lon + radius_degree,
            target.lat + radius_degree,
        ],
        datetime=target.datetime,
        count=frame_count,
    )
    if not success:
        return success

    logger.info("🪄")

    return True
