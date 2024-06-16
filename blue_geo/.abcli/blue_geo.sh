#! /usr/bin/env bash

function blue_geo() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        blue_geo_leaf "$@"
        blue_geo_node "$@"
        blue_geo task "$@"
        return
    fi

    if [ "$task" == "task" ]; then
        local options=$2
        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            abcli_show_usage "blue_geo task [<thing_1+thing_2>|all]" \
                "task things."
            return
        fi

        local what=$(abcli_option "$options" what what)

        python3 -m blue_geo \
            task \
            --what "$what" \
            "${@:3}"

        return
    fi

    abcli_generic_task \
        plugin=blue_geo,task=$task \
        "${@:2}"
}

abcli_log $(blue_geo version --show_icon 1)


