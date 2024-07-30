#! /usr/bin/env bash

function blue_geo_catalog_query_read() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="all,download,len"
        local args="[--count <count>]$ABCUL[--delim <delim>]$ABCUL[--index <index>]$ABCUL[--prefix <prefix>]$ABCUL[--suffix <suffix>]$ABCUL[--contains <contains>]$ABCUL[--notcontains <not-contains>]"
        abcli_show_usage "@catalog query read$ABCUL[$options]$ABCUL[.|<object-name>]$ABCUL$args" \
            "read query results in <object-name>."
        return
    fi

    local do_download=$(abcli_option_int "$options" download 0)
    local show_len=$(abcli_option_int "$options" len 0)
    local do_all=$(abcli_option_int "$options" all 0)

    local object_name=$(abcli_clarify_object $2 .)

    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    local extra_args=""
    [[ "$do_all" == 1 ]] &&
        extra_args="--count -1"

    python3 -m blue_geo.catalog.query \
        read \
        --object_name $object_name \
        --show_len $show_len \
        $extra_args \
        "${@:3}"
}
