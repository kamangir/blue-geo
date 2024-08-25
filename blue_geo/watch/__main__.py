import os
from typing import List, Union
import argparse
from blueness import module
from abcli import file
from blue_geo import NAME, VERSION
from blue_geo.watch.targets import TargetList
from blue_geo.watch.workflow import generate_workflow
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)

list_of_tasks = "generate_workflow|get"


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help=list_of_tasks,
)

# get
parser.add_argument(
    "--what",
    default="",
    type=str,
    help="args|catalog|collection|list_of_targets",
)
parser.add_argument(
    "--count",
    type=int,
    default=-1,
    help="-1: all",
)
parser.add_argument(
    "--log",
    default=1,
    type=int,
    help="0|1",
)
parser.add_argument(
    "--delim",
    type=str,
    default=",",
)

# generate_workflow
parser.add_argument(
    "--job_name",
    type=str,
)
parser.add_argument(
    "--processing_options",
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
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = args.task in list_of_tasks
target_list = TargetList(os.path.join(file.path(__file__), "targets.yaml"))
if args.task == "generate_workflow":
    success = generate_workflow(
        query_object_name=args.query_object_name,
        job_name=args.job_name,
        object_name=args.object_name,
        processing_options=args.processing_options,
    )
elif args.task == "get":
    output: Union[str, List[str]] = []

    if args.what == "args":
        output = target_list.targets.get(args.catalog).args
    elif args.what == "catalog":
        output = target_list.targets.get(args.catalog).catalog
    elif args.what == "collection":
        output = target_list.targets.get(args.catalog).collection
    elif args.what == "list_of_targets":
        output = list(target_list.targets.keys())
    else:
        success = False

    if args.count != -1 and isinstance(output, list):
        output = output[: args.count]

    if success:
        if args.log:
            logger.info(
                "{:,} {}(s): {}".format(
                    len(output),
                    args.what,
                    delim.join(output),
                )
                if isinstance(output, list)
                else output
            )
        else:
            print(delim.join(output) if isinstance(output, list) else output)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
