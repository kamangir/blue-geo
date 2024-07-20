#! /usr/bin/env bash

function blue_geo_datacube_ingest() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        blue_geo_ingest_firms "$@"
        return
    fi

    # refactor

    local function_name=blue_geo_ingest_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "-@datacube: ingest: $task: command not found."
    return 1
}
