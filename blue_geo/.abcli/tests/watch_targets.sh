#! /usr/bin/env bash

function test_blue_geo_watch_targets_cat() {
    abcli_download - $BLUE_GEO_WATCH_TARGET_LIST

    blue_geo_watch_targets cat \
        chilcotin-river-landslide-test
}

function test_blue_geo_watch_targets_download() {
    blue_geo_watch_targets_download
}

function test_blue_geo_watch_targets_test() {
    abcli_download - $BLUE_GEO_WATCH_TARGET_LIST

    blue_geo_watch_targets test
}
