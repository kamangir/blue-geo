#! /usr/bin/env bash

function blue_geo_datacube_list() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="types"
        local args="[--delim space]$ABCUL[--log 0]"
        abcli_show_usage "@datacube list$ABCUL[$options]$ABCUL$args" \
            "list datacube types."
        return
    fi
    python3 -m blue_geo.datacube \
        list_of_types \
        "$@"
}

function blue_geo_datacube_ls() {
    blue_geo_datacube_list "$@"
}
