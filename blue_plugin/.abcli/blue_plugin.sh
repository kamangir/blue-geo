#! /usr/bin/env bash

function blue_plugin() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        blue_plugin_leaf "$@"
        blue_plugin_node "$@"
        blue_plugin task "$@"
        return
    fi

    if [ "$task" == "task" ]; then
        local options=$2
        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            abcli_show_usage "blue_plugin task [<thing_1+thing_2>|all]" \
                "task things."
            return
        fi

        local what=$(abcli_option "$options" what what)

        python3 -m blue_plugin \
            task \
            --what "$what" \
            "${@:3}"

        return
    fi

    abcli_generic_task \
        plugin=blue_plugin,task=$task \
        "${@:2}"
}

abcli_log $(blue_plugin version --show_icon 1)
