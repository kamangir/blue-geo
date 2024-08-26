#! /usr/bin/env bash

function blue_geo_catalog_browse() {
    local catalog=$1

    if [[ "$catalog" == help ]]; then
        for catalog in $(echo $blue_geo_list_of_catalogs | tr , " "); do
            [[ "$catalog" == generic ]] &&
                continue
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
        local url_args=$(python3 -m blue_geo.catalog get \
            --catalog $catalog \
            --what url_args)
        abcli_show_usage "@catalog browse $catalog$ABCUL$url_args" \
            "browse $catalog."
        return
    fi

    local url=$(python3 -m blue_geo.catalog get \
        --catalog $catalog \
        --what "url:$what" \
        "${@:3}")

    abcli_browse $url
}
