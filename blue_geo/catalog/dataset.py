from blueness import module

from blue_objects.metadata import post_to_object

from blue_geo import NAME
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


def prep_dataset(
    module_name: str,
    query_object_name: str,
) -> bool:
    logger.info(
        "{}.prep_dataset: {} @ {}...".format(
            NAME,
            module_name,
            query_object_name,
        )
    )

    return all(
        post_to_object(
            query_object_name,
            keyword,
            value,
        )
        for keyword, value in {
            "kind": "distributed",
            "module_name": module_name,
            "source": "catalog_query",
        }.items()
    )
