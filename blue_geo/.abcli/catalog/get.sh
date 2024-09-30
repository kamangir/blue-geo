#! /usr/bin/env bash

function blue_geo_catalog_get() {
    local what=$1

    if [[ "$what" == help ]]; then
        abcli_show_usage_2 blue_geo catalog get
        return
    fi

    python3 -m blue_geo.catalog \
        get \
        --what "$what" \
        "${@:2}"
}
