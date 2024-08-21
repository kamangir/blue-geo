import argparse
from blueness import module
from blue_geo import NAME, VERSION
from blue_geo.catalog.generic.generic.classes import (
    GenericDatacube,
)
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="query",
)
parser.add_argument(
    "--log",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--save",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--visualize",
    type=int,
    default=1,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "query":
    success = GenericDatacube.query(
        object_name=args.object_name,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
