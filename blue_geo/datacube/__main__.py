import argparse
from blueness import module
from abcli import file
from blue_geo import NAME, VERSION
from blue_geo.catalog import get_datacube
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="get|ingest|list",
)
parser.add_argument(
    "--what",
    default="",
    type=str,
    help="catalog|template",
)
parser.add_argument(
    "--scope",
    default="metadata",
    type=str,
    help=DatacubeScope.help,
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
parser.add_argument(
    "--log",
    type=int,
    default=1,
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
    elif args.what == "template":
        output = datacube.QGIS_template

    print(output)
elif args.task == "ingest":
    datacube = get_datacube(datacube_id=args.datacube_id)
    success, _ = datacube.ingest(
        dryrun=args.dryrun == 1,
        overwrite=args.overwrite == 1,
        scope=args.scope,
    )
elif args.task == "list":
    success = True
    datacube = get_datacube(datacube_id=args.datacube_id)

    list_of_files = datacube.list_of_files(DatacubeScope(args.scope))

    if args.exists == 1:
        list_of_files = [
            filename
            for filename in list_of_files
            if file.exist(datacube.full_filename(filename))
        ]

    if args.count != -1:
        list_of_files = list_of_files[: args.count]

    if args.log:
        logger.info("{} file(s)".format(len(list_of_files)))
        for index, filename in enumerate(list_of_files):
            logger.info(f"#{index:03d} - {filename}")
    else:
        print(delim.join(list_of_files))
else:
    success = None

sys_exit(logger, NAME, args.task, success)
