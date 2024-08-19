#! /usr/bin/env bash

function blue_geo_catalog_query_generic() {
    local options=$1

    local catalog=$(abcli_option "$options" catalog generic)

    local list_of_datacube_classes=$(blue_geo_catalog list \
        datacube_classes \
        --catalog $catalog \
        --delim , \
        --log 0)
    local default_datacube_class=$(blue_geo_catalog list \
        datacube_classes \
        --catalog $catalog \
        --count 1 \
        --delim , \
        --log 0)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local datacube_class
        for datacube_class in $(echo $list_of_datacube_classes | tr , " "); do
            blue_geo_catalog_query_${catalog}_${datacube_class} "$@"
        done
        return 0
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local datacube_class=$(abcli_option_choice "$options" $list_of_datacube_classes $default_datacube_class)

    if [[ ",$list_of_datacube_classes," != *",$datacube_class,"* ]]; then
        abcli_log_error "-@catalog: query: $catalog: $datacube_class: datacube_class not found."
        return 1
    fi

    if [[ "$2" == "help" ]]; then
        blue_geo_catalog_query_${catalog}_${datacube_class} help
        return
    fi

    abcli_log "🌐 query: $catalog/$datacube_class"

    blue_geo_catalog_query_${catalog}_${datacube_class} "$@"
}

abcli_source_path - caller,suffix=/query
