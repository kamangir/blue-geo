#! /usr/bin/env bash

function blue_geo_datacube_ingest_firms_area() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options=$blue_geo_datacube_ingest_options
        "$EOP~copy_template,dryrun,$EOPE"
        abcli_show_usage "blue_geo ingest firms_area$ABCUL[$options]$ABCUL[.|<object-name>]$ABCUL" \
            "firms -ingest-> <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local object_name=$(abcli_clarify_object $2 .)

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.datacube.firms.area \
        ingest \
        --object_name $object_name \
        "${@:3}"
}
