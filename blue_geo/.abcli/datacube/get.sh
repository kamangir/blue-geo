#! /usr/bin/env bash

function blue_geo_datacube_get() {
    local what=$1

    if [[ "$what" == "help" ]]; then
        options="catalog"
        abcli_show_usage "@datacube get$ABCUL[$options]$ABCUL.|<object-name>" \
            "get <object-name> catalog."

        options="template"
        abcli_show_usage "@datacube get$ABCUL[$options]$ABCUL<catalog>" \
            "get <catalog> template."

        return
    fi

    local extra_args=""

    if [[ "$what" == "catalog" ]]; then
        local object_name=$(abcli_clarify_object $2 .)
        extra_args="--object_name $object_name ${@:3}"
    elif [[ "$what" == "template" ]]; then
        extra_args="--catalog $2 ${@:3}"
    else
        extra_args="${@:2}"
    fi

    python3 -m blue_geo.datacube \
        get \
        --what "$what" \
        "$extra_args"
}
