from blueness import module
from blue_options import string
from blue_objects.metadata import get_from_object
from blueflow.workflow.generic import Workflow

from blue_geo import NAME
from blue_geo.watch.targets.target import Target
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


def generate_workflow(
    algo_options: str,
    query_object_name: str,
    job_name: str,
    object_name: str,
    map_options: str,
    reduce_options: str,
) -> bool:
    list_of_datacube_id = get_from_object(
        query_object_name,
        "datacube_id",
    )

    suffix = string.pretty_date(
        include_date=False,
        as_filename=True,
        unique=True,
    )

    logger.info(
        "{}.generate_workflow @ {}: [{} X {} datacube(s)]/{}: -[{} @ {} + {}]-> {}".format(
            NAME,
            algo_options,
            query_object_name,
            len(list_of_datacube_id),
            suffix,
            map_options,
            reduce_options,
            job_name,
            object_name,
        )
    )

    workflow = Workflow(job_name)

    workflow.G.add_node("reduce")
    workflow.G.nodes["reduce"]["command_line"] = " ".join(
        [
            "blueflow_workflow monitor",
            "node=reduce",
            job_name,
            "blue_geo_watch_reduce",
            f",{algo_options},suffix={suffix},{reduce_options}",
            query_object_name,
            object_name,
        ]
    )

    for offset in range(len(list_of_datacube_id)):
        node = f"map-{offset:03d}"

        workflow.G.add_node(node)

        workflow.G.nodes[node]["command_line"] = " ".join(
            [
                "blueflow_workflow monitor",
                f"node={node}",
                job_name,
                "blue_geo_watch_map",
                f",{algo_options},offset={offset:03d},suffix={suffix},{map_options}",
                query_object_name,
            ]
        )

        workflow.G.add_edge("reduce", node)

    return workflow.save()
