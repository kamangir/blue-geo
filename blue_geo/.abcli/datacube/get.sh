#! /usr/bin/env bash

function blue_geo_datacube_get() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="catalog|template"
        abcli_show_usage "@datacube get$ABCUL[$options]$ABCUL[.|<object-name>]" \
            "get datacube properties."
        return
    fi

    local what=$(abcli_option_choice "$options" catalog,template void)

    local object_name=$(abcli_clarify_object $2 .)

    python3 -m blue_geo.datacube \
        get \
        --what "$what" \
        --object_name $object_name \
        "${@:3}"
}
