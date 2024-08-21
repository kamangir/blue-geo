import argparse
from blueness import module
from blue_geo import NAME, VERSION
from blue_geo.catalog import get_datacube
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="get|ingest",
)
parser.add_argument(
    "--what",
    default="",
    type=str,
    help="catalog|template",
)
parser.add_argument(
    "--datacube_id",
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
    datacube = get_datacube(datacube_id=args.datacube_id)

    output = f"unknown-{args.what}"
    if args.what == "template":
        output = datacube.QGIS_template
    elif args.what == "catalog":
        output = datacube.catalog.name

    print(output)
elif args.task == "ingest":
    datacube = get_datacube(datacube_id=args.datacube_id)
    success, _ = datacube.ingest(object_name=datacube.datacube_id)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
