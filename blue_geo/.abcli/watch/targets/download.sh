#! /usr/bin/env bash

function blue_geo_watch_targets_download() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage_2 blue_geo watch targets download
        return
    fi

    abcli_download - $BLUE_GEO_WATCH_TARGET_LIST

    python3 -m blue_geo.watch.targets list
}
