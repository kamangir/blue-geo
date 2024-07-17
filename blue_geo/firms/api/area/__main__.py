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
    help="get|ingest",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--source",
    type=str,
    default=Source.default().name,
    help="|".join(Source.values()),
)
parser.add_argument(
    "--area",
    type=str,
    default=Area.default().name,
    help="|".join(Area.values()),
)
parser.add_argument(
    "--date",
    type=str,
    default=(datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d"),
    help="yyyy-mm-dd",
)
parser.add_argument(
    "--depth",
    type=int,
    default=1,
    help="1..10",
)
parser.add_argument(
    "--what",
    type=str,
    default="area",
    help="area|source",
)
parser.add_argument(
    "--values",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--delim",
    type=str,
    default="|",
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = False
if args.task == "get":
    what = Area if args.what == "area" else Source if args.what == "source" else None
    what = what.default() if what else None
    print((delim.join(what.values()) if args.values else what.name) if what else None)
    success = True
elif args.task == "ingest":
    api_request = APIRequest(
        area=Area[args.area],
        source=Source[args.source],
        depth=args.depth,
        date=args.date,
    )

    success, _ = api_request.ingest(object_name=args.object_name)
else:
    success = None

sys_exit(logger, NAME, args.task, success)