import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_geo import NAME
from blue_geo.catalog.default import add_default_arguments
from blue_geo.catalog import get_datacube_class_in_catalog
from blue_geo.catalog.generic.generic.stac import STACDatacube
from blue_geo.catalog.copernicus.sentinel_2.classes import CopernicusSentinel2Datacube
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="query",
)
add_default_arguments(STACDatacube.query_args, parser)
parser.add_argument(
    "--object_name",
    type=str,
    default="",
)
parser.add_argument(
    "--catalog",
    type=str,
)
parser.add_argument(
    "--collection",
    type=str,
)
args = parser.parse_args()


success = False
if args.task == "query":
    datacube_class = get_datacube_class_in_catalog(
        args.catalog,
        args.collection,
    )

    assert issubclass(datacube_class, STACDatacube)

    success = datacube_class.query(
        object_name=args.object_name,
        bbox=(
            [float(item) for item in args.bbox.split(",") if item]
            if args.bbox
            else [
                args.lon - args.radius,
                args.lat - args.radius,
                args.lon + args.radius,
                args.lat + args.radius,
            ]
        ),
        datetime=args.datetime,
        count=args.count,
        keyword=args.keyword,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
