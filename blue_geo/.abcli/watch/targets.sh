#! /usr/bin/env bash

function blue_geo_watch_targets() {
    local task=$1
    [[ "$task" == "copy" ]] && task="cp"

    local function_name=blue_geo_watch_targets_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [[ "$task" == "edit" ]]; then
        abcli_code $ABCLI_OBJECT_ROOT/$BLUE_GEO_WATCH_TARGET_LIST/metadata.yaml
        return
    fi

    if [[ ",get,list," == *","$task","* ]]; then
        python3 -m blue_geo.watch.targets "$@"
        return
    fi

    if [[ "$task" == "test" ]]; then
        python3 -m blue_geo.watch.targets test
        return
    fi

    abcli_log_error "@targets: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /targets
