#! /usr/bin/env bash

function blue_geo_catalog_ingest_firms() {
    local ingest_options=$1

    local options=$2

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        ingest_options=$blue_geo_datacube_ingest_options
        options="dryrun"
        abcli_show_usage "@datacube ingest firms$ABCUL[$ingest_options]$ABCUL[.|<object-name>]$ABCUL[$options]$ABCUL[<args>]" \
            "firms -ingest-> <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local object_name=$(abcli_clarify_object $2 .)

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.catalog.firms \
        ingest \
        --object_name $object_name \
        "${@:3}"
}
