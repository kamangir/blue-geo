import os
import argparse
from blueness import module
from abcli import file
from blue_geo import NAME, VERSION
from blue_geo.target import Target
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)

list_of_tasks = "list"


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
    help="targets",
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
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = args.task in list_of_tasks
if args.task == "list":
    output = []

    if args.what == "targets":
        target = Target()
        success = target.load(os.path.join(file.path(__file__), "targets.yaml"))
        if success:
            output = list(target.items.keys())
    else:
        success = False

    if args.count != -1:
        output = output[: args.count]

    if success:
        if args.log:
            logger.info(
                "{:,} {}(s): {}".format(
                    len(output),
                    args.what,
                    delim.join(output),
                )
            )
        else:
            print(delim.join(output))
else:
    success = None

sys_exit(logger, NAME, args.task, success)
