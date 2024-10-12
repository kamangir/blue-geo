#! /usr/bin/env bash

function blue_geo_datacube() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        blue_geo_datacube_crop "$@"
        blue_geo_datacube_generate "$@"
        blue_geo_datacube_get "$@"
        blue_geo_datacube_ingest "$@"
        blue_geo_datacube_list "$@"
        return
    fi

    local function_name=blue_geo_datacube_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "-@datacube: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /datacube
