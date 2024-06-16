#! /usr/bin/env bash

function blue_geo_leaf() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="dryrun,upload"
        local args="[--<keyword> <value>]$ABCUL[--<keyword> <value>]"
        abcli_show_usage "blue_geo leaf$ABCUL[$options]$ABCUL<object-name>$ABCUL$args" \
            "blue-geo leaf <object-name>."
        return
    fi

    echo "blue-geo: leaf: 🪄"
}


