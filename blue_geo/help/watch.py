import os
from typing import List

from blue_options.terminal import show_usage, xtra
from blue_objects import file
from notebooks_and_scripts.workflow.runners import list_of_runners

from blue_geo.watch.targets.classes import TargetList


def get(
    tokens: List[str],
    mono: bool,
) -> str:
    if tokens[0] == "map":
        options = "".join(
            [
                xtra("dryrun,~download,"),
                "offset=<offset>,suffix=<suffix>",
                xtra(",~upload"),
            ]
        )

        return show_usage(
            [
                "@geo watch map",
                f"[{options}]",
                "[.|<query-object-name>]",
            ],
            "@geo watch map <query-object-name> @ <offset> -> /<suffix>.",
            mono=mono,
        )

    if tokens[0] == "reduce":
        options = "".join(
            [
                xtra("dryrun,~download,"),
                "publish,suffix=<suffix>",
                xtra(",~upload"),
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

    if tokens[0] == "targets":

        if tokens[1] in ["copy", "cp"]:
            options = "-"
            return show_usage(
                [
                    "@geo watch targets cp|copy",
                    f"[{options}]",
                    "[..|<object-name-1>]",
                    "[.|<object-name-2>]",
                ],
                "copy <object-name-1>/target -> <object-name-2>.",
                mono=mono,
            )

        args = [
            "[--delim space]",
            "[--target_name <target>]",
            "[--what <catalog|collection|exists|query_args>]",
        ]
        usage_1 = show_usage(
            ["@geo watch targets get"] + args,
            "get <target> info.",
            mono=mono,
        )

        args = [
            "[--catalog <catalog>]",
            "[--collection <collection>]",
            "[--count <count>]",
            "[--delim <space>]",
        ]
        usage_2 = show_usage(
            ["@geo watch targets list"] + args,
            "list targets.",
            mono=mono,
        )

        args = [
            "[--target_name <target>]",
            "[--object_name <object-name>]",
        ]
        usage_3 = show_usage(
            ["@geo watch targets save"] + args,
            "save <target> -> <object-name>.",
            mono=mono,
        )

        return "\n".join(
            [
                usage_1,
                usage_2,
                usage_3,
            ]
        )

    options = xtra("dryrun")

    target_list = TargetList(
        os.path.join(file.path(__file__), "../watch/targets.yaml"),
    )
    target_options = "".join(
        [
            xtra("<query-object-name>,"),
            "target={}".format("|".join(target_list.get_list())),
        ]
    )

    workflow_options = "".join(
        [
            xtra("dryrun,"),
            "to={}".format("|".join(list_of_runners())),
        ]
    )

    map_options = xtra("dryrun")

    reduce_options = "".join(
        [
            xtra("dryrun,~gif,"),
            "publish",
        ]
    )

    return show_usage(
        [
            "@geo watch",
            f"[{options}]",
            f"[{target_options}]",
            f"[{workflow_options}]",
            f"[{map_options}]",
            f"[{reduce_options}]",
            "[-|<object-name>]",
        ],
        "watch target -> <object-name>.",
        mono=mono,
    )
