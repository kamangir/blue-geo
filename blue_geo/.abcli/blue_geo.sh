#! /usr/bin/env bash

function blue_geo() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        return
    fi

    abcli_generic_task \
        plugin=blue_geo,task=$task \
        "${@:2}"
}

abcli_log $(blue_geo version --show_icon 1)
