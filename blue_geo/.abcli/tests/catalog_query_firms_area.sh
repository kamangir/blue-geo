#! /usr/bin/env bash

function test_blue_geo_catalog_query_firms_area() {
    local options=$1

    local object_name=firms-$(abcli_string_timestamp_short)

    blue_geo catalog query firms \
        ingest \
        $object_name \
        area \
        --date 2024-07-20
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo catalog query read len $object_name) \
        1
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo catalog query read - $object_name) \
        $BLUE_GEO_TEST_DATACUBE_FIRMS_AREA
}
