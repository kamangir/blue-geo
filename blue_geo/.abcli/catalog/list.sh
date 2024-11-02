#! /usr/bin/env bash

function blue_geo_catalog_list() {
    local options=$1
    local what=$(abcli_option_choice "$options" catalogs,collections,datacubes,datacube_classes catalogs)

    python3 -m blue_geo.catalog \
        list \
        --what "$what" \
        "${@:2}"
}

function blue_geo_catalog_ls() {
    blue_geo_catalog_list "$@"
}

function blue_geo_catalog_load_all() {
    abcli_log_list $blue_geo_list_of_catalogs \
        --delim , \
        --before "🌐 loading" \
        --after "catalog(s)"

    local catalog
    local list_of_collections
    for catalog in $(echo $blue_geo_list_of_catalogs | tr , " "); do
        abcli_source_caller_suffix_path /$catalog ignore_error

        list_of_datacube_classes=$(blue_geo_catalog list \
            datacube_classes \
            --catalog $catalog \
            --log 0)
        abcli_log_list "$list_of_datacube_classes" \
            --before "🧊 $GREEN$catalog$NC: loaded" \
            --after "collection(s)"
    done

    return 0
}

export blue_geo_list_of_catalogs=$(blue_geo_catalog_list catalogs --log 0)

blue_geo_catalog_load_all
