import argparse
from blueness import module
from blue_geo import NAME, VERSION
from blue_geo.catalog.ukraine_timemap.datacube import UkraineTimemapDatacube
from blue_geo.catalog import get_datacube
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help="ingest|query",
)
parser.add_argument(
    "--log",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--save",
    type=int,
    default=1,
    help="0|1",
)
parser.add_argument(
    "--visualize",
    type=int,
    default=1,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "ingest":
    datacube = UkraineTimemapDatacube(datacube_id=args.object_name)
    success, _ = datacube.ingest(
        object_name=datacube.datacube_id,
        do_save=args.save == 1,
        do_visualize=args.visualize == 1,
        log=args.log == 1,
    )
elif args.task == "query":
    success = UkraineTimemapDatacube.query(
        object_name=args.object_name,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
