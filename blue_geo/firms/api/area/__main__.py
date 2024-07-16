import argparse
from datetime import datetime, timedelta
from blue_geo import VERSION
from blue_geo.firms.api.area import NAME
from blue_geo.firms.api.area.enums import Area, Source
from blue_geo.firms.api.area.classes import APIRequest
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="ingest",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--source",
    type=str,
    default=Source.default.name,
    help="|".join(Source.default.values),
)
parser.add_argument(
    "--area",
    type=str,
    default=Area.default.name,
    help="|".join(Area.default.values),
)
parser.add_argument(
    "--date",
    type=str,
    default=(datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d"),
    help="yyyy-mm-dd",
)
parser.add_argument(
    "--day_range",
    type=int,
    default=1,
    help="1..10",
)

args = parser.parse_args()

success = False
if args.task == "ingest":
    api_request = APIRequest(
        area=Area[args.area],
        source=Source[args.source],
        day_range=args.day_range,
        date=args.date,
    )

    success = api_request.ingest(object_name=args.object_name)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
