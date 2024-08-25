import os
from typing import List, Union
import argparse
from blueness import module
from abcli import file
from blue_geo import NAME, VERSION
from blue_geo.watch.targets.classes import TargetList
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)

list_of_tasks = "get"

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help=list_of_tasks,
)
parser.add_argument(
    "--what",
    default="",
    type=str,
    help="args|catalog|collection|list",
)
parser.add_argument(
    "--count",
    type=int,
    default=-1,
    help="-1: all",
)
parser.add_argument(
    "--log",
    default=0,
    type=int,
    help="0|1",
)
parser.add_argument(
    "--delim",
    type=str,
    default=",",
)
parser.add_argument(
    "--target_name",
    type=str,
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = args.task in list_of_tasks
target_list = TargetList(os.path.join(file.path(__file__), "../targets.yaml"))
if args.task == "get":
    output: Union[str, List[str]] = []

    if args.what == "args":
        output = [
            f"--{arg} {value}"
            for arg, value in target_list.targets.get(args.target_name).args.items()
        ]
    elif args.what == "catalog":
        output = target_list.targets.get(args.target_name).catalog
    elif args.what == "collection":
        output = target_list.targets.get(args.target_name).collection
    elif args.what == "list":
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
