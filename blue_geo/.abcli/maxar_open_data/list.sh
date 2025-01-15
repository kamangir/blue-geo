#! /usr/bin/env bash

function blue_geo_maxar_open_data_list() {
    local options=$1

    python3 -m blue_geo.maxar_open_data \
        list \
        "${@:2}"
}
