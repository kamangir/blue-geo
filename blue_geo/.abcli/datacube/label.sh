#! /usr/bin/env bash

function blue_geo_datacube_label() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_open_QGIS=$(abcli_option_int "$options" QGIS 1)
    local do_rasterize=$(abcli_option_int "$options" rasterize 1)
    local do_sync=$(abcli_option_int "$options" sync 1)
    local do_upload=$(abcli_option_int "$options" upload 0)

    local datacube_id=$(abcli_clarify_object $2 .)

    if [[ "$do_sync" == 1 ]]; then
        abcli_eval dryrun=$do_dryrun \
            python3 -m blue_geo.datacube.label \
            sync \
            --datacube_id $datacube_id
        [[ $? -ne 0 ]] && return 1
    fi

    if [[ "$do_open_QGIS" == 1 ]]; then
        abcli_open QGIS $datacube_id

        abcli_wait "ready to save the labels?"
        [[ $? -ne 0 ]] && return 1
    fi

    if [[ "$do_rasterize" == 1 ]]; then
        abcli_eval dryrun=$do_dryrun \
            python3 -m blue_geo.datacube.label \
            rasterize \
            --datacube_id $datacube_id
        [[ $? -ne 0 ]] && return 1
    fi

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $datacube_id

    return 0
}
