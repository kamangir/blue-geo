import argparse
from blue_geo import VERSION
from blue_geo.datacube.catalogs import list_of_datacube_classes
from blue_geo import env
from blue_geo.datacube.catalogs import catalog_of
from blue_geo.datacube import NAME
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="get|list_of_catalogs",
)
parser.add_argument(
    "--delim",
    type=str,
    default=",",
)
parser.add_argument(
    "--log",
    default=1,
    type=int,
    help="0|1",
)
parser.add_argument(
    "--what",
    default="",
    type=str,
    help="catalog|template",
)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--catalog",
    type=str,
    default="",
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = False
if args.task == "get":
    success = True
    output = f"unknown-{args.what}"
    if args.what == "template":
        output = env.QGIS_TEMPLATES.get(args.catalog, output)
    elif args.what == "catalog":
        _, output = catalog_of(datacube_id=args.object_name)

    print(output)
elif args.task == "list_of_catalogs":
    success = True
    output = list(
        {datacube_class.catalog for datacube_class in list_of_datacube_classes}
    )

    if args.log:
        logger.info(f"{len(output):,} catalog(s): {delim.join(output)}")
    else:
        print(delim.join(output))
else:
    success = None

sys_exit(logger, NAME, args.task, success)
