#! /usr/bin/env bash

function test_blue_geo_catalog_query() {
    local options=$1
    local list_of_catalogs=$(echo $blue_geo_list_of_catalogs | tr , +)
    list_of_catalogs=$(abcli_option "$options" catalog $list_of_catalogs)

    local catalog
    local datacube_class
    for catalog in $(echo $list_of_catalogs | tr + " "); do
        [[ "$catalog" == generic ]] && continue

        local list_of_datacube_classes=$(blue_geo_catalog list \
            datacube_classes \
            --catalog $catalog \
            --delim , \
            --log 0)
        [[ $? -ne 0 ]] && return 1

        for datacube_class in $(echo $list_of_datacube_classes | tr , " "); do
            abcli_log "testing $catalog/$datacube_class/query ..."

            local object_name="bashtest-$catalog-$datacube_class-$(abcli_string_timestamp)"

            abcli_eval ,$options \
                blue_geo catalog query $catalog $datacube_class \
                ingest \
                $object_name
            [[ $? -ne 0 ]] && return 1

            abcli_assert \
                $(blue_geo catalog query read len $object_name) \
                0 \
                not
            [[ $? -ne 0 ]] && return 1

            local datacube_id=$(blue_geo catalog query read - $object_name)

            local public_name=datacube-$catalog-$datacube_class

            abcli_publish \
                as=$public_name,tar \
                $datacube_id
            [[ $? -ne 0 ]] && return 1

            abcli_publish \
                as=$public_name,suffix=.png \
                $datacube_id
            [[ $? -ne 0 ]] && return 1

            abcli_hr
        done
    done
    return 0
}
