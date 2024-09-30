import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_options.env import ABCUL
from blue_geo import NAME
from blue_geo.catalog.functions import (
    get_catalog_class,
    get_datacube_class_in_catalog,
    get_list_of_collections,
    get_list_of_datacube_classes,
)
from blue_geo.catalog.classes import list_of_catalogs
from blue_geo.catalog.default import as_list_of_args
from blue_geo.catalog.generic.stac.classes import STACCatalog
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)

list_of_tasks = "get|list"


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
parser.add_argument(
    "--datacube_class",
    type=str,
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = args.task in list_of_tasks
item_name = "item"
if args.task == "get":
    if args.what == "is_STAC":
        catalog_class = get_catalog_class(args.catalog)
        print(int(issubclass(catalog_class, STACCatalog)))
    elif args.what.startswith("url:"):
        catalog_class = get_catalog_class(args.catalog)
        print(
            catalog_class.url.get(
                args.what.split("url:", 1)[1],
                "",
            ),
        )
    elif args.what == "url_args":
        catalog_class = get_catalog_class(args.catalog)
        print("|".join(sorted([item for item in catalog_class.url if item])))
    elif args.what == "list_of_args":
        datacube_class = get_datacube_class_in_catalog(
            args.catalog,
            args.datacube_class,
        )
        print(ABCUL.join(as_list_of_args(datacube_class.query_args)))
    else:
        print(f"unknown-{args.what}")
elif args.task == "list":
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
else:
    success = None

sys_exit(logger, NAME, args.task, success)
