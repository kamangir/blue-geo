import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_geo import NAME
from blue_geo.help.functions import get as get_help

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "--command",
    type=str,
)
parser.add_argument(
    "--mono",
    type=int,
    default=0,
    help="0|1",
)
args = parser.parse_args()

tokens = args.command.strip().split(" ") + 10 * [""]

content = get_help(
    tokens=tokens,
    mono=args.mono == 1,
)

if content:
    print(content)


sys_exit(None, NAME, "help", bool(content))
