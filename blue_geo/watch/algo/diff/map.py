from blueness import module
from blue_objects import file
from blue_objects.metadata import post_to_object, get_from_object

from blue_geo import NAME
from blue_geo.watch.workflow.common import load_watch
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def map_function(
    query_object_name: str,
    suffix: str,
    offset: str,
) -> bool:
    offset_int = int(offset)

    object_name = f"{query_object_name}-{suffix}-{offset}"

    list_of_datacube_id = get_from_object(
        query_object_name,
        "datacube_id",
        [],
    )
    if len(list_of_datacube_id) < offset_int + 1:
        logger.warning(f"offset={offset}: datacube-id not found.")
        return True
    datacube_id = list_of_datacube_id[offset_int]

    success, target, list_of_files = load_watch(object_name)
    if not success or not list_of_files:
        return success
    filename = list_of_files[0]

    logger.info(
        "{}.map: {} #{} @ {} -> {}".format(
            NAME,
            target,
            offset,
            datacube_id,
            object_name,
        )
    )

    logger.info("🪄")

    return post_to_object(
        object_name,
        "map",
        {
            "algo": "diff",
            "inputs": {
                "offset": offset,
            },
            "datacube_id": datacube_id,
            "filename": file.name_and_extension(filename),
            "target": target.__dict__,
            "usable": success,
        },
    )
