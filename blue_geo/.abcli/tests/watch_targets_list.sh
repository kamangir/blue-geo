#! /usr/bin/env bash

function test_blue_geo_watch_targets_list() {
    abcli_download - $BLUE_GEO_WATCH_TARGET_LIST

    abcli_assert \
        $(blue_geo_watch_targets list \
            --delim + \
            --log 0) \
        - non-empty
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_watch_targets list \
            --catalog_name SkyFox \
            --collection Venus \
            --delim + \
            --log 0) \
        - non-empty
}
