#! /usr/bin/env bash

function blue_geo_catalog_get() {
    local what=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        what="is_STAC|url:<...>|url_args|list_of_args"
        local args="[--catalog <catalog>]"
        abcli_show_usage "@catalog get$ABCUL[$what]$ABCUL$args" \
            "get catalog properties."
        return
    fi

    python3 -m blue_geo.catalog \
        get \
        --what "$what" \
        "${@:2}"
}
