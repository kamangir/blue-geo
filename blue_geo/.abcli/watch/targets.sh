#! /usr/bin/env bash

function blue_geo_watch_targets() {
    local task=$1
    [[ "$task" == "copy" ]] && task="cp"

    if [[ "$task" == "help" ]]; then
        abcli_show_usage_2 blue_geo watch targets
        return
    fi

    local function_name=blue_geo_watch_targets_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [ "$2" == "help" ]; then
        abcli_show_usage_2 blue_geo watch targets $task
        return
    fi

    if [[ ",get,list,save," == *","$task","* ]]; then
        python3 -m blue_geo.watch.targets "$@"
        return
    fi

    if [[ ",download,upload," == *","$task","* ]]; then
        abcli_$task - $BLUE_GEO_WATCH_TARGET_LIST
        return
    fi

    abcli_log_error "@geo: watch: $task: command not found."
    return 1
}

abcli_source_path - caller,suffix=/targets
