import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_geo import NAME
from blue_geo.datacube.modalities import options as modality_options
from blue_geo.watch.algo.modality.map import map_function
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
    "--content_threshold",
    type=float,
    default=0.5,
    help="0..1",
)
parser.add_argument(
    "--modality",
    default=modality_options[0],
    type=str,
    help="|".join(modality_options),
)
args = parser.parse_args()

success = args.task in list_of_tasks
if args.task == "map":
    success = map_function(
        query_object_name=args.query_object_name,
        suffix=args.suffix,
        offset=args.offset,
        modality=args.modality,
    )
elif args.task == "reduce":
    success = reduce_function(
        query_object_name=args.query_object_name,
        suffix=args.suffix,
        object_name=args.object_name,
        content_threshold=args.content_threshold,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
