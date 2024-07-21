#! /usr/bin/env bash

function blue_geo_datacube_query_read() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="download,len"
        local args="$blue_geo_datacube_query_read_args"
        abcli_show_usage "@datacube query read$ABCUL[$options]$ABCUL[.|<object-name>]$ABCUL$args" \
            "read query results in <object-name>."
        return
    fi

    local do_download=$(abcli_option_int "$options" download 0)
    local show_len=$(abcli_option_int "$options" len 0)

    local object_name=$(abcli_clarify_object $2 .)

    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    python3 -m blue_geo.datacube.query \
        read \
        --object_name $object_name \
        --show_len $show_len \
        "${@:3}"
}
