#! /usr/bin/env bash

function blue_geo_catalog_list() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="-"
        local args="[--delim space]$ABCUL[--log 0]"
        abcli_show_usage "@catalog list$ABCUL[$options]$ABCUL$args" \
            "list catalogs."
        return
    fi

    python3 -m blue_geo.catalog \
        list \
        "${@:2}"
}

function blue_geo_catalog_ls() {
    blue_geo_catalog_list "$@"
}

function blue_geo_catalog_load_all() {
    abcli_log_list $blue_geo_catalog_list \
        --delim , \
        --before "🌐 loading" \
        --after "catalog(s)"

    local catalog
    for catalog in $(echo $blue_geo_catalog_list | tr , " "); do
        abcli_log "🧊 $catalog"
        abcli_source_path - caller,civilized,suffix=/$catalog
    done

    return 0
}

export blue_geo_catalog_list=$(blue_geo_catalog_list - --log 0)

blue_geo_catalog_load_all
