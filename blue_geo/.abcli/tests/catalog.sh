#! /usr/bin/env bash

function test_blue_geo_catalog_browse() {
    local options=$1

    local catalog
    for catalog in $(echo $blue_geo_catalog_list | tr , " "); do
        abcli_eval ,$options \
            blue_geo catalog browse $catalog
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}

function test_blue_geo_catalog_get_list_of_collections() {
    local options=$1

    local catalog
    for catalog in $(echo $blue_geo_catalog_list | tr , " "); do
        abcli_eval ,$options \
            blue_geo catalog get \
            list_of_collections \
            --catalog $catalog \
            --delim , \
            --log 0
        [[ $? -ne 0 ]] && return 1

        abcli_eval ,$options \
            blue_geo catalog get \
            list_of_collections \
            --catalog $catalog \
            --count 1 \
            --delim , \
            --log 0
        [[ $? -ne 0 ]] && return 1
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
    for catalog in $(echo $blue_geo_catalog_list | tr , " "); do
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
