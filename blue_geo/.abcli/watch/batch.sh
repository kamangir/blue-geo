#! /usr/bin/env bash

function blue_geo_watch_batch() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage_2 blue_geo watch batch
        return
    fi

}
