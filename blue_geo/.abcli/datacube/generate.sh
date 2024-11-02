#! /usr/bin/env bash

function blue_geo_datacube_generate() {
    local options=$1
    local dryrun=$(abcli_option_int "$options" dryrun 0)

    local datacube_id=$(abcli_clarify_object $2 .)

    local command=$(python3 -m blue_geo.datacube \
        generate \
        --datacube_id $datacube_id \
        "${@:3}")

    abcli_eval dryrun=$dryrun \
        "$command"
}
