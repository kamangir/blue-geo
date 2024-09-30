#! /usr/bin/env bash

function blue_geo_catalog_browse() {
    local catalog=$1

    if [[ "$catalog" == help ]]; then
        for catalog in $(echo $blue_geo_list_of_catalogs | tr , " "); do
            [[ "$catalog" == generic ]] && continue
            blue_geo_catalog_browse $catalog "$@"
        done
        return
    fi

    if [[ ",$blue_geo_list_of_catalogs," != *",$catalog,"* ]]; then
        abcli_log_error "-@catalog: browse: $catalog: catalog not found."
        return 1
    fi

    local what=$2

    if [[ "$what" == help ]]; then
        abcli_show_usage_2 blue_geo catalog browse $catalog
        return
    fi

    local url=$(blue_geo_catalog_get \
        "url:$what" \
        --catalog $catalog \
        "${@:3}")

    abcli_browse $url
}
