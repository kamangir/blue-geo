import argparse
from blueness import module
from abcli import file
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
    help="get:catalog|list_of_files|template, ingest: all|metadata|quick|<suffix>",
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
parser.add_argument(
    "--suffix",
    default="",
    type=str,
    help="<.jp2+.tif+.tiff>",
)
parser.add_argument(
    "--delim",
    type=str,
    default="+",
)
parser.add_argument(
    "--count",
    type=int,
    default=-1,
    help="-1: all",
)
parser.add_argument(
    "--exists",
    type=int,
    default=0,
    help="0|1",
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = False
if args.task == "get":
    success = True
    datacube = get_datacube(datacube_id=args.datacube_id)

    output = f"unknown-{args.what}"
    if args.what == "catalog":
        output = datacube.catalog.name
    elif args.what == "list_of_files":
        list_of_files = [
            filename
            for filename in datacube.list_of_files()
            if any(filename.endswith(suffix) for suffix in args.suffix.split("+"))
        ]

        if args.exists == 1:
            list_of_files = [
                filename
                for filename in list_of_files
                if file.exist(datacube.full_filename(filename))
            ]

        if args.count != -1:
            list_of_files = list_of_files[: args.count]

        output = delim.join(list_of_files)
    elif args.what == "template":
        output = datacube.QGIS_template

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
