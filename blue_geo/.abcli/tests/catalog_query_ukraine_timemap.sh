#! /usr/bin/env bash

function test_blue_geo_ukraine_timemap() {
    local options=$1

    local object_name=ukraine-timemap-$(abcli_string_timestamp_short)

    blue_geo catalog query ukraine_timemap \
        ingest \
        $object_name
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo catalog query read len $object_name) \
        1
    [[ $? -ne 0 ]] && return 1

    local datacube_id=$(blue_geo catalog query read - $object_name)

    abcli_publish \
        as=ukraine_timemap,tar \
        $datacube_id
    [[ $? -ne 0 ]] && return 1

    abcli_publish \
        as=ukraine_timemap,suffix=.png \
        $datacube_id
}
