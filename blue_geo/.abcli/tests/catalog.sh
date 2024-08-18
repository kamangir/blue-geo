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

function test_blue_geo_catalog_list() {
    local options=$1

    abcli_eval ,$options \
        blue_geo catalog list \
        catalogs \
        --delim , \
        --log 0
    [[ $? -ne 0 ]] && return 1

    local catalog
    local what
    for catalog in $(echo $blue_geo_list_of_catalogs | tr , " "); do
        for what in datacubes datacubes datacube_classes; do
            abcli_eval ,$options \
                blue_geo catalog list \
                $what \
                --catalog $catalog \
                --delim , \
                --log 0
            [[ $? -ne 0 ]] && return 1
        done
    done

    return 0
}

function test_blue_geo_catalog_list() {
    local options=$1

    abcli_eval ,$options \
        blue_geo catalog list
}

function test_blue_geo_catalog_query() {
    local options=$1

    local catalog
    for catalog in $(echo $blue_geo_list_of_catalogs | tr , " "); do
        local object_name="bashtest-$(abcli_string_timestamp)"

        [[ "$catalog" == generic ]] && continue

        abcli_eval ,$options \
            blue_geo catalog query $catalog \
            ingest \
            $object_name
        [[ $? -ne 0 ]] && return 1

        abcli_assert \
            $(blue_geo catalog query read len $object_name) \
            1
        [[ $? -ne 0 ]] && return 1
    done
    return 0
}
