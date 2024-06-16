import argparse
from blue_plugin import VERSION
from blue_plugin.node import NAME
from blue_plugin.node.functions import func
from blue_plugin.logger import logger
from blueness.argparse.generic import sys_exit

parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="task",
)
parser.add_argument(
    "--arg",
    type=bool,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "task":
    success = func(args.arg)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
