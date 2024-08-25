from blueness import module
from notebooks_and_scripts.workflow.generic import Workflow
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
        "{}.generate_workflow: {}: -[{} @ {}]-> {}".format(
            NAME,
            query_object_name,
            processing_options,
            job_name,
            object_name,
        )
    )

    workflow = Workflow(job_name)

    workflow.G.add_node("combination")

    workflow.G.nodes["combination"]["command_line"] = "echo 🪄"

    logger.info("🪄")

    return workflow.save()
