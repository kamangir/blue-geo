from typing import List
import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_geo import NAME
from blue_geo.watch.targets.target_list import TargetList
from blue_geo.help.watch.targets import get_what_list
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)

list_of_tasks = "get|list|save|test"


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
    help=get_what_list,
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
    "--including_versions",
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

target_list = TargetList()

target = target_list.get(
    args.target_name,
    including_versions=args.including_versions == 1,
)

success = args.task in list_of_tasks
if args.task == "get":
    output: str = ""

    if args.what == "catalog":
        output = target.catalog
    elif args.what == "collection":
        output = target.collection
    elif args.what == "exists":
        output = "1" if target.name else "0"
    elif args.what == "one_liner":
        output = target.one_liner
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
        including_versions=args.including_versions == 1,
    )

    if args.count != -1:
        output = output[: args.count]

    if success:
        if args.log:
            logger.info("{:,} target(s).".format(len(output)))
            for index, target_name in enumerate(output):
                logger.info(f"#{index: 4} - {target_name}")
        else:
            print(delim.join(output))
elif args.task == "save":
    if args.target_name == "all":
        success = target_list.save(args.object_name)
    else:
        success = target.save(args.object_name)
elif args.task == "test":
    success = target_list.test()
else:
    success = None

sys_exit(logger, NAME, args.task, success)
