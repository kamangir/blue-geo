import argparse
from blueness import module
from blue_geo import NAME, VERSION
from blue_geo.catalog.default import add_default_arguments
from blue_geo.catalog.EarthSearch.sentinel_2_l1c.classes import (
    EarthSearchSentinel2L1CDatacube,
)
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="query",
)
add_default_arguments(EarthSearchSentinel2L1CDatacube.query_args, parser)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
args = parser.parse_args()


success = False
if args.task == "query":
    success = EarthSearchSentinel2L1CDatacube.query(
        object_name=args.object_name,
        bbox=(
            [float(item) for item in args.bbox.split(",") if item]
            if args.bbox
            else [
                args.lon - args.radius,
                args.lat - args.radius,
                args.lon + args.radius,
                args.lat + args.radius,
            ]
        ),
        datetime=args.datetime,
        count=args.count,
        keyword=args.keyword,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
