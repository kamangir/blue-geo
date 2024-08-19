#! /usr/bin/env bash

function test_blue_geo_catalog_browse() {
    local options=$1

    local catalog
    for catalog in $(echo $blue_geo_list_of_catalogs | tr , " "); do
        abcli_eval ,$options \
            blue_geo catalog browse $catalog
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}
