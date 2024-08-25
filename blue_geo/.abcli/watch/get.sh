#! /usr/bin/env bash

function blue_geo_watch_get() {
    local what=$1

    if [[ "$what" == help ]]; then
        local options="args|catalog|collection|list_of_targets"
        local args="[--target <target>]$ABCUL[--delim space]"
        abcli_show_usage "@geo watch get $(xwrap $options $args)" \
            "get @geo watch things."
        return
    fi

    python3 -m blue_geo.watch get \
        --what "$what" \
        "${@:2}"
}
