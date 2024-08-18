#! /usr/bin/env bash

function blue_geo_catalog_browse() {
    local options=$1

    local catalog=$(abcli_option_choice "$options" $blue_geo_list_of_catalogs firms)

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        for catalog in $(echo $blue_geo_list_of_catalogs | tr , " "); do
            blue_geo_catalog_browse_${catalog} "$@"
        done
        return
    fi

    abcli_log "@catalog: browsing $catalog ..."
    blue_geo_catalog_browse_${catalog} "${@:2}"
}
