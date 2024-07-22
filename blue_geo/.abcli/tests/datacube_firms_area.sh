#! /usr/bin/env bash

function test_blue_geo_datacube_firms_area() {
    local options=$1

    local object_name=firms-$(abcli_string_timestamp_short)

    blue_geo datacube query firms_area \
        ingest $object_name - \
        --date 2024-07-18

    abcli_assert \
        $(blue_geo datacube query read len $object_name) \
        1

    abcli_assert \
        $(blue_geo datacube query read - $object_name) \
        datacube-firms_area-world-MODIS_NRT-2024-07-18-1
}
