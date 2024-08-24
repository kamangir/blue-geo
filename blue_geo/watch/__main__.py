import os
import argparse
from blueness import module
from abcli import file
from blue_geo import NAME, VERSION
from blue_geo.watch.targets import TargetList
from blue_geo.watch.workflow import generate_workflow
from blue_geo.logger import logger
from blueness.argparse.generic import sys_exit

NAME = module.name(__file__, NAME)

list_of_tasks = "generate_workflow|list"


parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
parser.add_argument(
    "task",
    type=str,
    help=list_of_tasks,
)

# list
parser.add_argument(
    "--what",
    default="",
    type=str,
    help="targets",
)
parser.add_argument("--count", type=int, default=-1, help="-1: all")
parser.add_argument("--log", default=1, type=int, help="0|1")
parser.add_argument("--delim", type=str, default=",")

# generate_workflow
parser.add_argument(
    "--dryrun",
    default=0,
    type=int,
    help="0|1",
)
parser.add_argument(
    "--frame_count",
    default=10,
    type=int,
    help="<10>",
)
parser.add_argument(
    "--radius_degree",
    default=0.1,
    type=float,
    help="<0.1>",
)
parser.add_argument(
    "--job_name",
    type=str,
)
parser.add_argument(
    "--target_description",
    type=str,
)
parser.add_argument(
    "--process_options",
    type=str,
)
parser.add_argument(
    "--object_name",
    type=str,
)

args = parser.parse_args()

delim = " " if args.delim == "space" else args.delim

success = args.task in list_of_tasks
target_list = TargetList(os.path.join(file.path(__file__), "targets.yaml"))
if args.task == "generate_workflow":
    success = generate_workflow(
        job_name=args.job_name,
        object_name=args.object_name,
        frame_count=args.frame_count,
        radius_degree=args.radius_degree,
        target=target_list.get(args.target_description),
        process_options=args.process_options,
        dryrun=args.dryrun,
    )
elif args.task == "list":
    output = []

    if args.what == "targets":
        output = list(target_list.targets.keys())
    else:
        success = False

    if args.count != -1:
        output = output[: args.count]

    if success:
        if args.log:
            logger.info(
                "{:,} {}(s): {}".format(
                    len(output),
                    args.what,
                    delim.join(output),
                )
            )
        else:
            print(delim.join(output))
else:
    success = None

sys_exit(logger, NAME, args.task, success)
