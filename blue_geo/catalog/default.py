from typing import Dict, List
from argparse import ArgumentParser


def add_default_arguments(
    default_args: Dict[str, Dict],
    parser: ArgumentParser,
):
    for arg, values in default_args.items():
        parser.add_argument(
            f"--{arg}",
            type=values.get("type", str),
            default=values["default"],
            help=values["help"],
        )


def as_list_of_args(default_args: Dict[str, Dict]) -> List[str]:
    return sorted(
        [
            "[--{} {}]".format(
                arg,
                values["help"],
            )
            for arg, values in default_args.items()
        ]
    )
