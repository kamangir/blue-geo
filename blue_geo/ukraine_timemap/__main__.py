import argparse
from blue_geo import VERSION
from blue_geo.ukraine_timemap import NAME
from blue_geo.ukraine_timemap.functions import ingest
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
args = parser.parse_args()

success = False
if args.task == "ingest":
    success, _ = ingest(object_name=args.object_name)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
