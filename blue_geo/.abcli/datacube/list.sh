#! /usr/bin/env bash

function blue_geo_datacube_list() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="-"
        local args=$abcli_tag_search_args
        abcli_show_usage "@datacube list$ABCUL[$options]$ABCUL$args" \
            "list datacubes."
        return
    fi
    python3 -m blue_geo.datacube \
        list \
        "$@"
}

function blue_geo_datacube_ls() {
    blue_geo_datacube_list "$@"
}
