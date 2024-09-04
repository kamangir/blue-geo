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
        local url_args=$(blue_geo_catalog_get \
            url_args \
            --catalog $catalog)
        abcli_show_usage "@catalog browse $catalog$ABCUL$url_args" \
            "browse $catalog."
        return
    fi

    local url=$(blue_geo_catalog_get \
        "url:$what" \
        --catalog $catalog \
        "${@:3}")

    abcli_browse $url
}
