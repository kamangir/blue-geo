from blueness import module
from abcli.plugins.metadata import get_from_object
from notebooks_and_scripts.workflow.generic import Workflow
from blue_geo import NAME
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


def generate_workflow(
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

    logger.info(
        "{}.generate_workflow: {}[{} X]: -[{} @ {} + {}]-> {}".format(
            NAME,
            query_object_name,
            len(list_of_datacube_id),
            map_options,
            reduce_options,
            job_name,
            object_name,
        )
    )

    workflow = Workflow(job_name)

    workflow.G.add_node("reduction")
    workflow.G.nodes["reduction"]["command_line"] = " ".join(
        [
            "workflow monitor",
            "node=reduction",
            job_name,
            "blue_geo_watch_reduce",
            reduce_options,
            object_name,
        ]
    )

    for datacube_id in list_of_datacube_id:
        workflow.G.add_node(datacube_id)
        workflow.G.nodes[datacube_id]["command_line"] = " ".join(
            [
                "workflow monitor",
                f"node={datacube_id}",
                job_name,
                "blue_geo_watch_map",
                map_options,
                datacube_id,
                object_name,
            ]
        )
        workflow.G.add_edge("reduction", datacube_id)

    return workflow.save()
