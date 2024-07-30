#! /usr/bin/env bash

function blue_geo_catalog() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        blue_geo_catalog_browse "$@"
        blue_geo_catalog_get "$@"
        blue_geo_catalog_list "$@"
        blue_geo_catalog_query "$@"
        return
    fi

    local function_name=blue_geo_catalog_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "-@catalog: $task: command not found."
    return 1
}

abcli_source_path - caller,suffix=/catalog
