import argparse
from blueness import module
from blue_geo import NAME, VERSION
from blue_geo.catalog.default import add_default_arguments, as_list_of_args
from blue_geo.catalog.firms.area.enums import Area, Source
from blue_geo.catalog.firms.area.classes import FirmsAreaDatacube
from blue_geo.catalog.firms.area.default import args as default_args
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="get|query",
)
add_default_arguments(default_args, parser)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--what",
    type=str,
    default="area",
    help="list_of_args",
)
args = parser.parse_args()


success = False
if args.task == "get":
    output = f"unknown-{args.what}"

    if args.what == "list_of_args":
        output = as_list_of_args(default_args)

    print(output)
    success = True
elif args.task == "query":
    success = FirmsAreaDatacube.query(
        object_name=args.object_name,
        area=Area[args.area],
        source=Source[args.source],
        depth=args.depth,
        date=args.date,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
