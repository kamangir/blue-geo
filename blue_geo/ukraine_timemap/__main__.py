import argparse
from blueness import module
from blue_geo import NAME, VERSION
from blue_geo.ukraine_timemap.functions import ingest
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)


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
