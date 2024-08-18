import argparse
from blueness import module
from blue_geo import NAME, VERSION
from blue_geo.catalog.classes import (
    list_of_catalogs,
    get_list_of_collections,
    get_list_of_datacube_classes,
)
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
    help="catalogs,collections,datacubes==datacube_classes",
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
if args.task == "list":
    output = []

    if args.what == "catalogs":
        item_name = "catalog"
        output = list_of_catalogs
    elif args.what == "collections":
        item_name = "collection"
        output = get_list_of_collections(catalog_class=args.catalog)
    elif args.what in ["datacubes", "datacube_classes"]:
        item_name = "datacube class"
        output = [
            datacube_class.name
            for datacube_class in get_list_of_datacube_classes(
                catalog_class=args.catalog
            )
        ]
    else:
        success = False

    if args.count != -1:
        output = output[: args.count]
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
