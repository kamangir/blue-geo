import argparse
from blue_geo.QGIS import NAME
from blue_geo import VERSION
from blue_geo.QGIS.seed import generate_seed
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit


parser = argparse.ArgumentParser(
    f"python3 -m {NAME}",
    description=f"{NAME}-{VERSION}",
)
parser.add_argument(
    "task",
    type=str,
    help="generate_seed",
)
args = parser.parse_args()

success = False
if args.task == "generate_seed":
    success = seed = generate_seed()
    if success:
        print(seed)
else:
    success = None

sys_exit(logger, NAME, args.task, success)
