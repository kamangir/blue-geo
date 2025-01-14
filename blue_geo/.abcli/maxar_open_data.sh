#! /usr/bin/env bash

function blue_geo_maxar_open_data() {
    local task=$(abcli_unpack_keyword $1 help)

    local function_name=blue_geo_maxar_open_data_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "@maxar: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /maxar_open_data
