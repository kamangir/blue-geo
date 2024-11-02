#! /usr/bin/env bash

function blue_geo_catalog_browse() {
    local catalog=$1
    if [[ ",$blue_geo_list_of_catalogs," != *",$catalog,"* ]]; then
        abcli_log_error "@catalog: browse: $catalog: catalog not found."
        return 1
    fi

    local what=$2

    local url=$(blue_geo_catalog_get \
        "url:$what" \
        --catalog $catalog \
        "${@:3}")

    abcli_browse $url
}
