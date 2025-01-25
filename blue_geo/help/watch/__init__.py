from typing import List

from blue_options.terminal import show_usage, xtra
from blueflow.workflow.runners import list_of_runners
from blueflow.help.workflow import submit_options as workflow_submit_options
from blueflow.help.workflow import runner_details

from blue_geo.datacube.modalities import options as modality_options
from blue_geo.watch.targets.target_list import TargetList
from blue_geo.watch.algo import list_of_algo
from blue_geo.help.watch.targets import help_functions as help_targets


def help_(
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

    algo_options = "algo=<algo>,<algo-options>"

    workflow_options = "".join(
        [
            xtra("~submit | ", mono=mono),
            workflow_submit_options(
                mono=mono,
                cascade=True,
            ),
        ]
    )

    map_options = "".join(
        [
            xtra("dryrun,<map-options>", mono),
        ]
    )

    reduce_options = "".join(
        [
            "content=<0.5>",
            xtra(",dryrun,~gif,", mono),
            "publish",
            xtra(",<reduce-options>", mono=mono),
        ]
    )

    return show_usage(
        [
            "@geo",
            "watch",
            options if help_batch else f"[{options}]",
            f"[{target_options}]",
            f"[{algo_options}]",
            f"[{workflow_options}]",
            f"[{map_options}]",
            f"[{reduce_options}]",
            "[-|<object-name>]",
        ],
        "watch target -{}> <object-name>.".format("aws-batch-" if help_batch else ""),
        {
            "algo: diff | modality": [],
            "<algo-options>:": [
                "diff: modality=<modality>,range=<100.0>",
                "modality: modality=<modality>",
            ],
            "modality: {}".format(" | ".join(modality_options)): [],
            **runner_details,
            "target: {}".format(" | ".join(target_list.get_list())): [],
        },
        mono=mono,
    )


def help_batch(
    tokens: List[str],
    mono: bool,
) -> str:
    return help_(
        tokens=tokens,
        mono=mono,
        help_batch=True,
    )


def help_map(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "algo=<algo>",
            xtra(",dryrun,~download,", mono),
            "modality=<modality>,",
            "offset=<offset>,suffix=<suffix>",
            xtra(",~upload", mono),
        ]
    )

    return show_usage(
        [
            "@geo",
            "watch",
            "map",
            f"[{options}]",
            "[.|<query-object-name>]",
        ],
        "@geo watch map <query-object-name> @ <offset> -> /<suffix>.",
        mono=mono,
    )


def help_query(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "target=<target>",
            xtra(",~upload", mono=mono),
        ]
    )

    return show_usage(
        [
            "@geo",
            "watch",
            "query",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "query target -> <object-name>.",
        mono=mono,
    )


def help_reduce(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "algo=<algo>",
            xtra("dryrun,~download,", mono),
            "publish,suffix=<suffix>",
            xtra(",~upload", mono),
        ]
    )

    return show_usage(
        [
            "@geo",
            "watch",
            "reduce",
            f"[{options}]",
            "[..|<query-object-name>]",
            "[.|<object-name>]",
        ],
        "@geo watch reduce <query-object-name>/<suffix> -> <object-name>.",
        mono=mono,
    )


help_functions = {
    "": help_,
    "batch": help_batch,
    "map": help_map,
    "query": help_query,
    "reduce": help_reduce,
    "targets": help_targets,
}
