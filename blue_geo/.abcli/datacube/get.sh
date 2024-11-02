#! /usr/bin/env bash

function blue_geo_datacube_get() {
    local options=$1
    local what=$(abcli_option_choice "$options" catalog,raw,template void)

    local datacube_id=$(abcli_clarify_object $2 .)

    python3 -m blue_geo.datacube \
        get \
        --what "$what" \
        --datacube_id $datacube_id \
        "${@:3}"
}
