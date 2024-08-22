#! /usr/bin/env bash

function test_blue_geo_catalog_query_copernicus_sentinel_2() {
    local options=$1

    local object_name=copernicus-$(abcli_string_timestamp_short)

    blue_geo catalog query copernicus sentinel_2 ingest \
        $object_name \
        --date 2024-07-20/2024-07-30 \
        --count 1
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo catalog query read len $object_name) \
        1
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo catalog query read - $object_name) \
        $BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2
}
