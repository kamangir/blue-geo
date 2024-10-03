from typing import List

from blue_options.terminal import show_usage

from blue_geo.env import BLUE_GEO_WATCH_TARGET_LIST


def help_cp(
    tokens: List[str],
    mono: bool,
) -> str:
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


def help_download(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@geo watch targets download",
        ],
        "download watch targets.",
        {
            f"BLUE_GEO_WATCH_TARGET_LIST: {BLUE_GEO_WATCH_TARGET_LIST}": [],
        },
        mono=mono,
    )


def help_get(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--delim space]",
        "[--target_name <target>]",
        "[--what <catalog|collection|exists|query_args>]",
    ]
    return show_usage(
        ["@geo watch targets get"] + args,
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
    ]
    return show_usage(
        ["@geo watch targets list"] + args,
        "list targets.",
        mono=mono,
    )


def help_publish(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@geo watch targets publish",
        ],
        "publish watch targets.",
        {
            f"BLUE_GEO_WATCH_TARGET_LIST: {BLUE_GEO_WATCH_TARGET_LIST}": [],
        },
        mono=mono,
    )


def help_save(
    tokens: List[str],
    mono: bool,
) -> str:
    args = [
        "[--target_name <target>]",
        "[--object_name <object-name>]",
    ]
    return show_usage(
        ["@geo watch targets save"] + args,
        "save <target> -> <object-name>.",
        mono=mono,
    )


def help_upload(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@geo watch targets upload",
        ],
        "upload watch targets.",
        {
            f"BLUE_GEO_WATCH_TARGET_LIST: {BLUE_GEO_WATCH_TARGET_LIST}": [],
        },
        mono=mono,
    )


help_functions = {
    "cp": help_cp,
    "download": help_download,
    "get": help_get,
    "list": help_list,
    "publish": help_publish,
    "save": help_save,
    "upload": help_upload,
}
