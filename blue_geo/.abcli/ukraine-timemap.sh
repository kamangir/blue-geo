#! /usr/bin/env bash

function ukraine_timemap() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        ukraine_timemap_browse "$@"
        ukraine_timemap_ingest "$@"
        return
    fi

    if [[ "$task" == "init" ]]; then
        blue_geo "$@"
        return
    fi

    local function_name=ukraine_timemap_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "-ukraine_timemap: $task: command not found."
    return 1
}

abcli_source_path - caller,suffix=/ukraine-timemap
