from argparse import ArgumentParser
from abcli.logger import ABCUL
from typing import Dict


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


def as_list_of_args(default_args: Dict[str, Dict]) -> str:
    return ABCUL.join(
        sorted(
            [
                "[--{} {}]".format(
                    arg,
                    values["help"],
                )
                for arg, values in default_args.items()
            ]
        )
    )
