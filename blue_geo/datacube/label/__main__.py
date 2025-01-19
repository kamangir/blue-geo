import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_geo import NAME
from blue_geo.datacube.label.rasterize import rasterize_the_label
from blue_geo.datacube.label.sync import sync_the_label
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="rasterize | sync",
)
parser.add_argument(
    "--datacube_id",
    type=str,
)
parser.add_argument(
    "--verbose",
    type=int,
    default=0,
    help="0 | 1",
)
args = parser.parse_args()

success = False
if args.task == "rasterize":
    success = rasterize_the_label(
        datacube_id=args.datacube_id,
        verbose=args.verbose == 1,
    )
elif args.task == "sync":
    success = sync_the_label(
        datacube_id=args.datacube_id,
        verbose=args.verbose == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
