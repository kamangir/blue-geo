import argparse
from blue_geo import VERSION
from .classes import list_of_catalog_classes
from . import NAME
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="list",
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
if args.task == "list":
    success = True
    output = list({catalog_class.name for catalog_class in list_of_catalog_classes})

    if args.log:
        logger.info(f"{len(output):,} catalog(s): {delim.join(output)}")
    else:
        print(delim.join(output))
else:
    success = None

sys_exit(logger, NAME, args.task, success)
