#! /usr/bin/env bash

function blue_geo_datacube_list() {
    local datacube_id=$(abcli_clarify_object $1 .)

    python3 -m blue_geo.datacube \
        list \
        --datacube_id $datacube_id \
        "${@:2}"
}
