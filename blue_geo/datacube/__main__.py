import argparse
from blue_geo import VERSION
from blue_geo.catalog import get_datacube
from . import NAME
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="get",
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

success = False
if args.task == "get":
    success = True
    datacube = get_datacube(datacube_id=args.object_name)

    output = f"unknown-{args.what}"
    if args.what == "template":
        output = datacube.QGIS_template
    elif args.what == "catalog":
        output = datacube.catalog.name

    print(output)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
