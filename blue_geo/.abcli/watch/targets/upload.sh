#! /usr/bin/env bash

function blue_geo_watch_targets_upload() {
    python3 -m blue_geo.watch.targets test
    [[ $? -ne 0 ]] && return 1

    blue_geo_watch_targets \
        save \
        target=all \
        $BLUE_GEO_WATCH_TARGET_LIST
    [[ $? -ne 0 ]] && return 1

    abcli_upload - $BLUE_GEO_WATCH_TARGET_LIST
}
