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
    help="get:catalog|template, ingest: all|metadata|quick|<suffix>",
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
parser.add_argument(
    "--dryrun",
    default=0,
    type=int,
    help="0|1",
)
parser.add_argument(
    "--overwrite",
    default=0,
    type=int,
    help="0|1",
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
    success, _ = datacube.ingest(
        dryrun=args.dryrun == 1,
        overwrite=args.overwrite == 1,
        what=args.what if args.what else "metadata",
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
