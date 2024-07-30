#! /usr/bin/env bash

function blue_geo() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        blue_geo_catalog "$@"
        blue_geo_datacube "$@"
        blue_geo_QGIS "$@"
        ukraine_timemap "$@"
        return
    fi

    if [ "$task" == "pylint" ]; then
        abcli_${task} ignore=blue_geo/QGIS,plugin=blue_geo,$2 \
            "${@:3}"
        return
    fi

    abcli_generic_task \
        plugin=blue_geo,task=$task \
        "${@:2}"
}

abcli_log $(blue_geo version --show_icon 1)
