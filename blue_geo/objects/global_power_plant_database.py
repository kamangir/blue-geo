from blueness import module

from blue_geo import NAME
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


def ingest(
    object_name: str,
    version: str = "v1",
    dryrun: bool = False,
    overwrite: bool = False,
) -> bool:
    logger.info(
        "{}.ingest({}-{}) {}".format(
            NAME,
            object_name,
            version,
            ",".join(
                (["dryrun"] if dryrun else []) + (["overwrite"] if overwrite else [])
            ),
        )
    )

    logger.info("🪄")

    return True
