import argparse
from blueness import module
from blue_geo import NAME, VERSION
from blue_geo.catalog.classes import list_of_catalogs, get_collections
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)

list_of_tasks = "get,list"


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
    help="list_of_collections",
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
parser.add_argument(
    "--log",
    default=1,
    type=int,
    help="0|1",
)
parser.add_argument(
    "--catalog",
    default=list_of_catalogs[0],
    type=str,
    help="|".join(list_of_catalogs),
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = args.task in list_of_tasks
item_name = "item"
if args.task == "get":
    output = []

    if args.what == "list_of_collections":
        item_name = "collection"
        output = [
            datacube_class.name for datacube_class in get_collections(args.catalog)
        ]

    if args.count != -1:
        output = output[: args.count]
elif args.task == "list":
    item_name = "catalog"
    output = list_of_catalogs
else:
    success = None

if success:
    if args.log:
        logger.info(
            "{:,} {}(s): {}".format(
                len(output),
                item_name,
                delim.join(output),
            )
        )
    else:
        print(delim.join(output))

sys_exit(logger, NAME, args.task, success)
