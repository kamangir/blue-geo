#! /usr/bin/env bash

function blue_geo_datacube_generate() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage_2 blue_geo datacube generate
        return
    fi

    local dryrun=$(abcli_option_int "$options" dryrun 0)

    local datacube_id=$(abcli_clarify_object $2 .)

    local command=$(python3 -m blue_geo.datacube \
        generate \
        --datacube_id $datacube_id \
        "${@:3}")

    abcli_eval dryrun=$dryrun \
        "$command"
}
