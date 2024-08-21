import argparse
from blueness import module
from blue_geo import NAME, VERSION
from blue_geo.catalog.ukraine_timemap.ukraine_timemap.classes import (
    UkraineTimemapDatacube,
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
parser.add_argument(
    "--object_name",
    type=str,
)
args = parser.parse_args()

success = False
if args.task == "query":
    success = UkraineTimemapDatacube.query(object_name=args.object_name)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
