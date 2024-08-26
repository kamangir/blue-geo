import os
import argparse
from blueness import module
from abcli import file
from blue_geo import NAME, VERSION
from blue_geo.watch.targets.classes import TargetList
from blue_geo.watch.workflow.generation import generate_workflow
from blue_geo.watch.workflow.map import map_function
from blue_geo.watch.workflow.reduce import reduce_function
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)

list_of_tasks = "generate|map|reduce"


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help=list_of_tasks,
)
parser.add_argument(
    "--job_name",
    type=str,
)
parser.add_argument(
    "--map_options",
    type=str,
)
parser.add_argument(
    "--reduce_options",
    type=str,
)
parser.add_argument(
    "--datacube_id",
    type=str,
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--query_object_name",
    type=str,
)
parser.add_argument(
    "--suffix",
    type=str,
)
args = parser.parse_args()

success = args.task in list_of_tasks
target_list = TargetList(os.path.join(file.path(__file__), "targets.yaml"))
if args.task == "generate":
    success = generate_workflow(
        query_object_name=args.query_object_name,
        job_name=args.job_name,
        object_name=args.object_name,
        map_options=args.map_options,
        reduce_options=args.reduce_options,
    )
elif args.task == "map":
    success = map_function(
        args.datacube_id,
        args.object_name,
    )
elif args.task == "reduce":
    success = reduce_function(
        query_object_name=args.query_object_name,
        suffix=args.suffix,
        object_name=args.object_name,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
