#! /usr/bin/env bash

function blue_geo_catalog_query_firms_area() {
    local options=$1

    local catalog="firms"
    local collection="area"

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="$collection,dryrun"
        local args=$(python3 -m blue_geo.catalog.$catalog.$collection get --what list_of_args)
        abcli_show_usage "@catalog query $catalog$ABCUL[$blue_geo_catalog_query_options]$ABCUL[-|<object-name>]$ABCUL[$options]$ABCUL$args" \
            "$catalog/$collection -query-> <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local object_name=$(abcli_clarify_object $2 -)

    abcli_log "🌐 query: $catalog/$collection -> $object_name"

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.catalog.$catalog.$collection \
        query \
        --object_name $object_name \
        "${@:3}"

    return 0
}
