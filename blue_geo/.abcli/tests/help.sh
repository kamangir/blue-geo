#! /usr/bin/env bash

function test_blue_geo_help() {
    local options=$1

    local module
    for module in \
        "blue_geo" \
        \
        "blue_geo catalog" \
        "blue_geo catalog browse" \
        "blue_geo catalog list" \
        "blue_geo catalog query" \
        \
        "blue_geo datacube" \
        "blue_geo datacube get" \
        "blue_geo datacube ingest" \
        \
        "blue_geo QGIS" \
        "blue_geo QGIS_expressions" \
        "blue_geo QGIS_server" \
        \
        "blue_geo watch" \
        "blue_geo watch map" \
        "blue_geo watch reduce"; do
        abcli_eval ,$options \
            $module help
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}
