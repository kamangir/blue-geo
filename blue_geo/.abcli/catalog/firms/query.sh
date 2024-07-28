#! /usr/bin/env bash

function blue_geo_catalog_query_firms() {
    local options=$1

    local catalog="firms"

    local list_of_collectios=$(blue_geo_catalog get list_of_collections \
        --catalog $catalog \
        --delim , \
        --log 0)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="$list_of_collectios,dryrun"
        abcli_show_usage "@catalog query $catalog$ABCUL[$blue_geo_catalog_query_options]$ABCUL[-|<object-name>]$ABCUL[$options]$ABCUL[<args>]" \
            "$catalog -query-> <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local collection=$(abcli_option_choice "$options" $list_of_collectios area)

    if [[ ",$list_of_collectios," != *",$collection,"* ]]; then
        abcli_log_error "-@catalog: query: $catalog: $collection: collection not found."
        return 1
    fi

    if [[ "$2" == "help" ]]; then
        blue_geo_catalog_query_firms_${collection} help
        return
    fi

    blue_geo_catalog_query_firms_${collection} \
        ,$options \
        "${@:2}"
}

abcli_source_path - caller,suffix=/query
