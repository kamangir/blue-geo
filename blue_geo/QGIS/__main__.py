import argparse

from blueness import module
from blueness.argparse.generic import sys_exit
from blue_objects.env import ABCLI_OBJECT_ROOT

from blue_geo import NAME
from blue_geo.QGIS.seed import generate_seed
from blue_geo.QGIS.dependency import list_of_dependencies
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)

list_of_tasks = "generate_seed|list_dependencies"

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help=list_of_tasks,
)
parser.add_argument(
    "--delim",
    type=str,
    default="+",
)
parser.add_argument(
    "--filename",
    type=str,
)
parser.add_argument(
    "--verbose",
    type=int,
    default="0",
    help="0|1",
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = args.task in list_of_tasks.split("|")
if args.task == "generate_seed":
    print(generate_seed())
elif args.task == "list_dependencies":
    output = list_of_dependencies(
        filename=args.filename,
        ABCLI_OBJECT_ROOT=ABCLI_OBJECT_ROOT,
        verbose=args.verbose == 1,
    )

    print(delim.join(output))
else:
    success = None

sys_exit(logger, NAME, args.task, success)
