import argparse
from types import ModuleType

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
    help="get | ingest",
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
    default="",
    help="defaults to <object_name>.version",
)
parser.add_argument(
    "--what",
    default="template_name",
    type=str,
    help="template_name | version",
)
parser.add_argument(
    "--default",
    default="void",
    type=str,
)
parser.add_argument(
    "--overwrite",
    default=0,
    type=int,
    help="0|1",
)

args = parser.parse_args()

success = False
if args.task == "get":
    success = True
    output = args.default

    if args.object_name in special_objects:
        object_module: ModuleType = special_objects[args.object_name]

        if args.what == "template_name":
            output = object_module.template_name
        elif args.what == "version":
            output = object_module.version

    print(output)
elif args.task == "ingest":
    if args.object_name in special_objects:
        object_module: ModuleType = special_objects[args.object_name]

        version = args.version
        if not version:
            version = object_module.version

        success = object_module.ingest(
            object_name=args.object_name,
            version=version,
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
