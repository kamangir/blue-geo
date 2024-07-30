#! /usr/bin/env bash

function blue_geo_catalog_get() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="list_of_collections"
        local args="[--catalog <catalog>]$ABCUL[--count 1]$ABCUL[--delim ,]$ABCUL[--log 0]"
        abcli_show_usage "@catalog get$ABCUL[$options]$ABCUL$args" \
            "get list of collections in <catalog>."
        return
    fi

    local what=$(abcli_option_choice "$options" list_of_collections list_of_collections)

    python3 -m blue_geo.catalog \
        get \
        --what "$what" \
        "${@:2}"
}
