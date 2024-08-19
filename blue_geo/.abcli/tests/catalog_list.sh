#! /usr/bin/env bash

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
