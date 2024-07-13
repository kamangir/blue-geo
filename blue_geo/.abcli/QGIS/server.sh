#! /usr/bin/env bash

function blue_geo_QGIS_serve() {
    blue_geo_QGIS_server "$@"
}

function blue_geo_QGIS_server() {
    local options=$1
    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage "QGIS serve[r] [start]" \
            "start QGIS server."
        return
    fi

    local prompt="🌐 $(blue_geo version).QGIS server ... (^C to stop)"
    abcli_log $prompt

    abcli_badge "🌐"

    local filename
    cd $abcli_QGIS_path_server
    while true; do
        sleep 1
        for filename in *.command; do
            if [ -e "$filename" ]; then
                local command=$(cat $filename)
                abcli_log "$filename: $command"

                abcli_eval - "$command"
                rm -v $filename

                abcli_log $prompt
            fi
        done
    done
}
