import argparse
from blueness import module
from blue_geo import NAME, VERSION
from abcli.plugins.metadata import get_from_object
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="read",
)
parser.add_argument(
    "--count",
    type=int,
    default=1,
)
parser.add_argument(
    "--delim",
    type=str,
    default=",",
)
parser.add_argument(
    "--offset",
    type=int,
    default=0,
)
parser.add_argument(
    "--prefix",
    type=str,
    default="",
)
parser.add_argument(
    "--suffix",
    type=str,
    default="",
)
parser.add_argument(
    "--contains",
    type=str,
    default="",
)
parser.add_argument(
    "--notcontains",
    type=str,
    default="",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--log",
    default=0,
    type=int,
    help="0|1",
)
parser.add_argument(
    "--show_len",
    default=0,
    type=int,
    help="0|1",
)
args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = False
if args.task == "read":
    success = True
    output = get_from_object(
        args.object_name,
        "datacube_id",
        [],
    )

    output = [
        datacube_id
        for datacube_id in output
        if (not args.prefix or datacube_id.startswith(args.prefix))
        and (not args.suffix or datacube_id.endswith(args.suffix))
        and (not args.contains or args.contains in datacube_id)
        and (not args.notcontains or args.notcontains not in datacube_id)
    ]

    output = output[args.offset :]

    if args.count != -1:
        output = output[: args.count]

    if args.log:
        logger.info(
            "{:,} datacube-id(s){}".format(
                len(output),
                "" if args.show_len else f": {delim.join(output)}",
            )
        )
    else:
        print(len(output) if args.show_len else delim.join(output))
else:
    success = None

sys_exit(logger, NAME, args.task, success)
