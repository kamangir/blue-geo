#! /usr/bin/env bash

function blue_geo_catalog_query_generic() {
    local options=$1

    local catalog=$(abcli_option "$options" catalog generic)

    local list_of_collectios=$(blue_geo_catalog get list_of_collections \
        --catalog $catalog \
        --delim , \
        --log 0)
    local default_collection=$(blue_geo_catalog get list_of_collections \
        --catalog $catalog \
        --count 1 \
        --delim , \
        --log 0)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local collection
        for collection in $(echo $list_of_collectios | tr , " "); do
            blue_geo_catalog_query_${catalog}_${collection} "$@"
        done
        return 0
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local collection=$(abcli_option_choice "$options" $list_of_collectios $default_collection)

    if [[ ",$list_of_collectios," != *",$collection,"* ]]; then
        abcli_log_error "-@catalog: query: $catalog: $collection: collection not found."
        return 1
    fi

    if [[ "$2" == "help" ]]; then
        blue_geo_catalog_query_${catalog}_${collection} help
        return
    fi

    abcli_log "🌐 query: $catalog/$collection"

    blue_geo_catalog_query_${catalog}_${collection} "$@"
}

function blue_geo_catalog_query_generic_generic() {
    : # no query available.
}

function blue_geo_catalog_browse_generic() {
    : # no browse available.
}
