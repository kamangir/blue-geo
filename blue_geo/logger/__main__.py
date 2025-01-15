import argparse

from blueness import module
from blue_objects import objects
from blueness.argparse.generic import sys_exit

from blue_geo import NAME
from blue_geo.logger.geoimage import log_geoimage
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="log_geoimage",
)
parser.add_argument(
    "--filename",
    type=str,
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--log",
    type=int,
    default=1,
    help="0 | 1",
)
parser.add_argument(
    "--verbose",
    type=int,
    default=1,
    help="0 | 1",
)
parser.add_argument(
    "--header",
    type=str,
    default="",
)
parser.add_argument(
    "--footer",
    type=str,
    default="",
)

args = parser.parse_args()

success = False
if args.task == "log_geoimage":
    success = log_geoimage(
        filename=args.filename,
        object_name=args.object_name,
        header=[args.header] if args.header else [],
        footer=[args.footer] if args.footer else [],
        log=args.log == 1,
        verbose=args.verbose == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
