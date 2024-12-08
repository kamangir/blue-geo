#! /usr/bin/env bash

function test_blue_geo_ingest() {
    local options=$1
    local list_of_objects=$(abcli_option "$options" objects global-power-plant-database)

    local object_name
    for object_name in $(echo $list_of_objects | tr + " "); do

        blue_geo_ingest \
            upload,publish,$options \
            $object_name
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
