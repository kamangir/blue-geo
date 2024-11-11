#! /usr/bin/env bash

function test_blue_geo_watch_query() {
    local options=$1

    local list_of_targets=$(abcli_option "$options" target chilcotin-river-landslide-test+Leonardo-test)

    local target
    for target in $(echo $list_of_targets | tr + " "); do
        local object_name=test_blue_geo_watch_query-$target-$(abcli_string_timestamp)

        blue_geo_watch_query \
            target=$target \
            $object_name
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
