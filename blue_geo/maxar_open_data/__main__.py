import argparse

from blueness import module
from blue_objects import objects
from blueness.argparse.generic import sys_exit

from blue_geo import NAME
from blue_geo.maxar_open_data.classes import MaxarOpenDataClient
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="ingest | list",
)
parser.add_argument(
    "--datacube_id",
    type=str,
)
parser.add_argument(
    "--log",
    type=int,
    default=1,
    help="0 | 1",
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0 | 1",
)
parser.add_argument(
    "--delim",
    type=str,
    default=",",
)
parser.add_argument(
    "--count",
    type=int,
    default=-1,
    help="-1: all",
)

args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

client = MaxarOpenDataClient(
    verbose=args.verbose == 1,
)


success = False
if args.task == "ingest":
    success = client.ingest(
        datacube_id=args.datacube_id,
        log=args.log == 1,
        verbose=args.verbose == 1,
    )
elif args.task == "list":
    success = True

    list_of_collections = client.get_list_of_collections(
        log=args.log == 1,
    )

    if args.count != -1:
        list_of_collections = list_of_collections[: args.count]

    if args.log == 0:
        print(delim.join(list_of_collections))
else:
    success = None

sys_exit(logger, NAME, args.task, success)
