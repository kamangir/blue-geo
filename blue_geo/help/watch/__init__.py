from typing import List

from blue_options.terminal import show_usage, xtra
from notebooks_and_scripts.workflow.runners import list_of_runners

from blue_geo.watch.targets.target_list import TargetList
from blue_geo.datacube.modalities import options as modality_options
from blue_geo.help.watch.targets import help_functions as help_targets


def help_map(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,~download,", mono),
            "modality=<modality>,",
            "offset=<offset>,suffix=<suffix>",
            xtra(",~upload", mono),
        ]
    )

    return show_usage(
        [
            "@geo watch map",
            f"[{options}]",
            "[.|<query-object-name>]",
        ],
        "@geo watch map <query-object-name> @ <offset> -> /<suffix>.",
        {
            "modality: {},".format("|".join(modality_options)): [],
        },
        mono=mono,
    )


def help_reduce(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,~download,", mono),
            "publish,suffix=<suffix>",
            xtra(",~upload", mono),
        ]
    )

    return show_usage(
        [
            "@geo watch reduce",
            f"[{options}]",
            "[..|<query-object-name>]",
            "[.|<object-name>]",
        ],
        "@geo watch reduce <query-object-name>/<suffix> -> <object-name>.",
        mono=mono,
    )


def help_batch(
    tokens: List[str],
    mono: bool,
) -> str:
    return help(
        tokens=tokens,
        mono=mono,
        help_batch=True,
    )


def help(
    tokens: List[str],
    mono: bool,
    help_batch: bool = False,
) -> str:
    options = "".join(
        [
            "batch",
            xtra(",dryrun,name=<job-name>", mono),
        ]
    )

    target_list = TargetList()

    target_options = "".join(
        [
            xtra("<query-object-name> | ", mono),
            "target=<target>",
        ]
    )

    workflow_options = "".join(
        [
            xtra("dryrun,", mono),
            "to=<runner>",
        ]
    )

    map_options = "".join(
        [
            xtra("dryrun,", mono),
            "modality=<modality>",
        ]
    )

    reduce_options = "".join(
        [
            xtra("dryrun,~gif,", mono),
            "publish",
        ]
    )

    return show_usage(
        [
            "@geo watch",
            options if help_batch else f"[{options}]",
            f"[{target_options}]",
            f"[{workflow_options}]",
            f"[{map_options}]",
            f"[{reduce_options}]",
            "[-|<object-name>]",
        ],
        "watch target -{}> <object-name>.".format("aws-batch-" if help_batch else ""),
        {
            "modality: {}".format("|".join(modality_options)): [],
            "runner: {}".format("|".join(list_of_runners())): [],
            "target: {}".format("|".join(target_list.get_list())): [],
        },
        mono=mono,
    )


help_functions = {
    "": help,
    "batch": help_batch,
    "map": help_map,
    "reduce": help_reduce,
    "targets": help_targets,
}
