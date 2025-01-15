#! /usr/bin/env bash

function blue_geo_maxar_open_data_ingest() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local datacube_id=$(abcli_clarify_object $2 .)

    abcli_eval ,$options \
        python3 -m blue_geo.maxar_open_data \
        ingest \
        --datacube_id $datacube_id \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $datacube_id

    return $status
}
