#! /usr/bin/env bash

function blue_geo_gdal() {
    local task=$(abcli_unpack_keyword $1 help)

    local function_name=blue_geo_gdal_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "@gdal: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /gdal
