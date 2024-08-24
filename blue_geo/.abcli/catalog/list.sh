#! /usr/bin/env bash

function blue_geo_catalog_list() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local args

        options="catalogs"
        args="[--count 1]$ABCUL[--delim ,]$ABCUL[--log 0]"
        abcli_show_usage "@catalog list$ABCUL[$options]$ABCUL$args" \
            "list catalogs."

        options="collections|datacubes==datacube_classes"
        args="[--catalog <catalog>]$ABCUL$args"
        abcli_show_usage "@catalog list$ABCUL[$options]$ABCUL$args" \
            "list $options in <catalog>."
        return
    fi

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
        abcli_source_path - caller,civilized,suffix=/$catalog

        list_of_datacube_classes=$(blue_geo_catalog list \
            datacube_classes \
            --catalog $catalog \
            --log 0)
        abcli_log_list "$list_of_datacube_classes" \
            --before "🧊 $GREEN$catalog$NC: loaded" \
            --after "datacube class(es)"
    done

    return 0
}

export blue_geo_list_of_catalogs=$(blue_geo_catalog_list catalogs --log 0)

blue_geo_catalog_load_all
