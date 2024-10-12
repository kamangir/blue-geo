from typing import List

from blue_options.terminal import show_usage

from blue_geo.env import BLUE_GEO_WATCH_TARGET_LIST
from blue_geo.watch.targets.target_list import TargetList

get_what_list = "catalog|collection|exists|one_liner|query_args"


def help_cat(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@targets cat",
            "<target-name>",
        ],
        "cat <target-name>.",
        mono=mono,
    )


def help_cp(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "-"
    return show_usage(
        [
            "@targets cp|copy",
            f"[{options}]",
            "[..|<object-name-1>]",
            "[.|<object-name-2>]",
        ],
        "copy <object-name-1>/target -> <object-name-2>.",
        mono=mono,
    )


def help_download(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "open,QGIS"
    return show_usage(
        [
            "@targets download",
            f"[{options}]",
        ],
        "download watch targets.",
        {
            f"$BLUE_GEO_WATCH_TARGET_LIST: {BLUE_GEO_WATCH_TARGET_LIST}": [],
        },
        mono=mono,
    )


def help_edit(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@targets edit",
        ],
        "edit watch targets.",
        {
            TargetList.filename(): [],
        },
        mono=mono,
    )


def help_get(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--delim space]",
        "[--including_versions 0]",
        "[--target_name <target>]",
        f"[--what <{get_what_list}>]",
    ]
    return show_usage(
        ["@targets get"] + args,
        "get <target> info.",
        mono=mono,
    )


def help_list(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--catalog <catalog>]",
        "[--collection <collection>]",
        "[--count <count>]",
        "[--delim <space>]",
        "[--including_versions 0]",
    ]
    return show_usage(
        ["@targets list"] + args,
        "list targets.",
        mono=mono,
    )


def help_open(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "QGIS"
    return show_usage(
        [
            "@targets open",
            f"[{options}]",
        ],
        "open targets.",
        mono=mono,
    )


def help_publish(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@targets publish",
        ],
        "publish watch targets.",
        {
            f"$BLUE_GEO_WATCH_TARGET_LIST: {BLUE_GEO_WATCH_TARGET_LIST}": [],
        },
        mono=mono,
    )


def help_save(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "target=all|<target-name>"
    return show_usage(
        [
            "@targets save",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "save target(s) -> <object-name>.",
        mono=mono,
    )


def help_test(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@targets test",
        ],
        "test watch targets.",
        {
            f"$BLUE_GEO_WATCH_TARGET_LIST: {BLUE_GEO_WATCH_TARGET_LIST}": [],
        },
        mono=mono,
    )


def help_upload(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@targets upload",
        ],
        "upload watch targets.",
        {
            f"$BLUE_GEO_WATCH_TARGET_LIST: {BLUE_GEO_WATCH_TARGET_LIST}": [],
        },
        mono=mono,
    )


help_functions = {
    "cat": help_cat,
    "cp": help_cp,
    "download": help_download,
    "edit": help_edit,
    "get": help_get,
    "list": help_list,
    "open": help_open,
    "publish": help_publish,
    "save": help_save,
    "test": help_test,
    "upload": help_upload,
}
