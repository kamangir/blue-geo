#! /usr/bin/env bash

function blue_geo_datacube_get() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="catalog|template"
        abcli_show_usage "@datacube get$ABCUL[$options]$ABCUL[.|<datacube-id>]" \
            "get datacube properties."

        options="list_of_files"
        local args="[--count 1]$ABCUL[--delim +]$ABCUL[--suffix <.jp2+.tif+.tiff>]"
        abcli_show_usage "@datacube get$ABCUL[$options]$ABCUL[.|<datacube-id>]$ABCUL$args" \
            "get list of datacube files."
        return
    fi

    local what=$(abcli_option_choice "$options" catalog,list_of_files,template void)

    local datacube_id=$(abcli_clarify_object $2 .)

    python3 -m blue_geo.datacube \
        get \
        --what "$what" \
        --datacube_id $datacube_id \
        "${@:3}"
}
