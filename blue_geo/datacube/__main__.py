import argparse
from blue_geo import VERSION
from blue_geo.datacube.catalogs import list_of
from blue_geo.ukraine_timemap import NAME
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="list_of_catalogs",
)
parser.add_argument(
    "--delim",
    type=str,
    default=",",
)
parser.add_argument(
    "--log",
    default=1,
    type=int,
    help="0|1",
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = False
if args.task == "list_of_catalogs":
    success = True
    output = list_of

    if args.log:
        logger.info(f"{len(output):,} catalog(s): {delim.join(output)}")
    else:
        print(delim.join(output))
else:
    success = None

sys_exit(logger, NAME, args.task, success)
