import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_geo import NAME
from blue_geo.watch.algo.diff.map import map_function
from blue_geo.watch.algo.modality.reduce import reduce_function
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)

list_of_tasks = "map|reduce"


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help=list_of_tasks,
)
parser.add_argument(
    "--offset",
    type=str,
    default="000",
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
parser.add_argument(
    "--depth",
    type=int,
    default=2,
)
parser.add_argument(
    "--range",
    type=float,
    default=100.0,
)
args = parser.parse_args()

success = args.task in list_of_tasks
if args.task == "map":
    success = map_function(
        query_object_name=args.query_object_name,
        suffix=args.suffix,
        offset=args.offset,
        depth=args.depth,
        range=args.range,
    )
elif args.task == "reduce":
    success = reduce_function(
        query_object_name=args.query_object_name,
        suffix=args.suffix,
        object_name=args.object_name,
        content_threshold=-1,
        list_of_suffix=["histogram"],
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
