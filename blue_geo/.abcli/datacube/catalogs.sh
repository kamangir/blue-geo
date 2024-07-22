#! /usr/bin/env bash

function blue_geo_datacube_list() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="catalogs"
        local args="[--delim space]$ABCUL[--log 0]"
        abcli_show_usage "@datacube list$ABCUL[$options]$ABCUL$args" \
            "list catalogs."
        return
    fi

    python3 -m blue_geo.datacube \
        list_of_catalogs \
        "${@:2}"
}

function blue_geo_datacube_ls() {
    blue_geo_datacube_list "$@"
}

function blue_geo_datacube_load_catalogs() {
    abcli_log_list $blue_geo_datacube_list_of_catalogs \
        --delim , \
        --before "🌐 loading" \
        --after "datacube catalog(s)"

    local catalog
    for catalog in $(echo $blue_geo_datacube_list_of_catalogs | tr , " "); do
        abcli_log "🧊 $catalog"
        abcli_source_path - caller,civilized,suffix=/$catalog
    done

    return 0
}

export blue_geo_datacube_list_of_catalogs=$(blue_geo_datacube_list catalogs --log 0)

blue_geo_datacube_load_catalogs
