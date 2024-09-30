import os
from typing import List, Union
import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from blue_objects import file

from blue_geo import NAME
from blue_geo.watch.targets.classes import TargetList, Target
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)

list_of_tasks = "get|list|save"

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help=list_of_tasks,
)
parser.add_argument(
    "--what",
    default="",
    type=str,
    help="catalog|collection|exists|query_args",
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
parser.add_argument(
    "--target_name",
    type=str,
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--catalog_name",
    type=str,
)
parser.add_argument(
    "--collection",
    type=str,
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

target_list = TargetList(
    os.path.join(file.path(__file__), "../targets.yaml"),
)

target = target_list.targets.get(args.target_name, Target())

success = args.task in list_of_tasks
if args.task == "get":
    output: str = ""

    if args.what == "catalog":
        output = target.catalog
    elif args.what == "collection":
        output = target.collection
    elif args.what == "exists":
        output = "1" if target.name else "0"
    elif args.what == "query_args":
        output = target.query_args_as_str()
    else:
        success = False

    if success:
        if args.log:
            logger.info(output)
        else:
            print(output)
elif args.task == "list":
    output = target_list.get_list(
        catalog_name=args.catalog_name,
        collection=args.collection,
    )

    if args.count != -1:
        output = output[: args.count]

    if success:
        if args.log:
            logger.info(
                "{:,} target(s): {}".format(
                    len(output),
                    delim.join(output),
                )
            )
        else:
            print(delim.join(output))
elif args.task == "save":
    success = target.save(args.object_name)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
