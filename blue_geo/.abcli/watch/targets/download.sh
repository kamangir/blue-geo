#! /usr/bin/env bash

function blue_geo_watch_targets_download() {
    local options=$1

    abcli_download - \
        $BLUE_GEO_WATCH_TARGET_LIST \
        "$@"

    abcli_list_log $(python3 -m blue_geo.watch.targets \
        list \
        --log 0) \
        --before "downloaded" \
        --after "target(s)"
}
