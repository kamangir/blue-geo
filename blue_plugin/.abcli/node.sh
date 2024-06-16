#! /usr/bin/env bash

function blue_plugin_node() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ "$task" == "help" ]; then
        blue_plugin_node_leaf "$@"
        return
    fi

    local function_name=blue_plugin_node_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    abcli_log_error "-blue_plugin: node: $task: command not found."
    return 1
}

abcli_source_path - caller,suffix=/node
