import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_geo import NAME
from blue_geo.catalog.default import add_default_arguments
from blue_geo.catalog.firms.area.enums import Area, Source
from blue_geo.catalog.firms.area.classes import FirmsAreaDatacube
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="query",
)
add_default_arguments(FirmsAreaDatacube.query_args, parser)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
args = parser.parse_args()


success = False
if args.task == "query":
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
