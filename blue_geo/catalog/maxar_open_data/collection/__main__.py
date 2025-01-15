import argparse
import datetime

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_geo import NAME
from blue_geo.catalog.default import add_default_arguments
from blue_geo.catalog.maxar_open_data.collection import MaxarOpenDataDatacube
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="query",
)
add_default_arguments(MaxarOpenDataDatacube.query_args, parser)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)

args = parser.parse_args()


success = False
if args.task == "query":
    success = MaxarOpenDataDatacube.query(
        object_name=args.object_name,
        collection_id=args.collection_id,
        lat=args.lat,
        lon=args.lon,
        radius=args.radius,
        start_date=args.start_date,
        end_date=args.end_date,
        count=args.count,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
