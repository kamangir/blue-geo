#! /usr/bin/env bash

function blue_geo_watch_targets_download() {
    local options=$1

    abcli_download overwrite \
        $BLUE_GEO_WATCH_TARGET_LIST \
        "$@"

    python3 -m blue_geo.watch.targets list
}
