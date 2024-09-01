from blueness import module
from abcli import file
from abcli.plugins.metadata import post_to_object
from blue_geo import NAME
from blue_geo.watch.workflow.common import load_watch
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def map_function(
    datacube_id: str,
    object_name: str,
) -> bool:
    success, target, list_of_files = load_watch(object_name)
    if not success or not list_of_files:
        return success
    filename = list_of_files[0]

    logger.info(
        "{}.map: {} @ {} -> {}".format(
            NAME,
            target,
            datacube_id,
            object_name,
        )
    )

    return post_to_object(
        object_name,
        "map",
        {
            "datacube_id": datacube_id,
            "filename": file.name_and_extension(filename),
            "target": target.__dict__,
        },
    )
