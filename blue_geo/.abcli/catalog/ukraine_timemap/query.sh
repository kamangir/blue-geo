#! /usr/bin/env bash

function blue_geo_catalog_query_ukraine_timemap() {
    local options=$1

    blue_geo_catalog_query_generic \
        $options,catalog=ukraine_timemap \
        "${@:2}"
}

function blue_geo_catalog_query_ukraine_timemap_ukraine_timemap() {
    local options=$1

    local catalog="ukraine_timemap"

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="dryrun"
        abcli_show_usage "@catalog query $catalog$ABCUL[$blue_geo_catalog_query_options]$ABCUL[-|<object-name>]$ABCUL[$options]" \
            "$catalog -query-> <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local object_name=$(abcli_clarify_object $2 -)

    abcli_log "🌐 query: $catalog -> $object_name"

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.catalog.$catalog \
        query \
        --object_name $object_name \
        "${@:3}"

    return 0
}
