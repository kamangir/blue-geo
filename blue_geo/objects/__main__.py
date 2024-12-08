import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_geo import NAME
from blue_geo.objects import special_objects
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="ingest",
)
parser.add_argument(
    "--object_name",
    default="",
    type=str,
    help=", ".join(special_objects.keys()),
)
parser.add_argument(
    "--version",
    type=str,
    default="v1",
)
parser.add_argument(
    "--dryrun",
    default=0,
    type=int,
    help="0|1",
)
parser.add_argument(
    "--overwrite",
    default=0,
    type=int,
    help="0|1",
)

args = parser.parse_args()

success = False
if args.task == "ingest":
    if args.object_name in special_objects:
        success = special_objects[args.object_name].ingest(
            object_name=args.object_name,
            version=args.version,
            dryrun=args.dryrun == 1,
            overwrite=args.overwrite == 1,
        )
    else:
        logger.error(
            "{}: object not found, expected one of {}.".format(
                args.object_name,
                ", ".join(special_objects.keys()),
            )
        )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
