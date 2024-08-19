#! /usr/bin/env bash

function blue_geo_catalog_query_generic_generic() {
    local options=$1

    local catalog=$(abcli_option "$options" catalog generic)
    local datacube_class=$(abcli_option "$options" datacube_class generic)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="dryrun,$datacube_class"
        local args=$(python3 -m blue_geo.catalog.$catalog.$datacube_class get --what list_of_args)
        abcli_show_usage "@catalog query $catalog$ABCUL[$blue_geo_catalog_query_options]$ABCUL[-|<object-name>]$ABCUL[$options]$ABCUL$args" \
            "$catalog/$datacube_class -query-> <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local object_name=$(abcli_clarify_object $2 -)

    abcli_log "🌐 query: $catalog/$datacube_class -> $object_name"

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.catalog.$catalog.$datacube_class \
        query \
        --object_name $object_name \
        "${@:3}"
}
