#! /usr/bin/env bash

function blue_geo_QGIS_server() {
    local prompt="🌐 $(blue_geo version).QGIS server ... (^C to stop)"
    abcli_log $prompt

    abcli_badge "🌐"

    local filename
    cd $BLUE_GEO_QGIS_PATH_SERVER
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
