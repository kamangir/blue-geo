#! /usr/bin/env bash

function blue_geo_datacube_list() {
    local datacube_id=$(abcli_clarify_object $1 .)

    if [[ "$datacube_id" == "help" ]]; then
        abcli_show_usage_2 blue_geo datacube list
        return
    fi

    python3 -m blue_geo.datacube \
        list \
        --datacube_id $datacube_id \
        "${@:2}"
}
