#! /usr/bin/env bash

function test_blue_geo_help() {
    local options=$1

    local module
    for module in \
        "blue_geo" \
        \
        "blue_geo catalog" \
        "blue_geo catalog browse" \
        "blue_geo catalog get" \
        "blue_geo catalog list" \
        "blue_geo catalog query" \
        \
        "blue_geo datacube" \
        "blue_geo datacube crop" \
        "blue_geo datacube generate" \
        "blue_geo datacube get" \
        "blue_geo datacube ingest" \
        "blue_geo datacube list" \
        \
        "blue_geo gdal" \
        \
        "blue_geo QGIS" \
        "blue_geo QGIS_expressions" \
        "blue_geo QGIS_server" \
        \
        "blue_geo watch" \
        "blue_geo watch batch" \
        "blue_geo watch map" \
        "blue_geo watch reduce" \
        \
        "blue_geo watch targets" \
        "blue_geo watch targets cat" \
        "blue_geo watch targets cp" \
        "blue_geo watch targets copy" \
        "blue_geo watch targets download" \
        "blue_geo watch targets edit" \
        "blue_geo watch targets get" \
        "blue_geo watch targets list" \
        "blue_geo watch targets publish" \
        "blue_geo watch targets save" \
        "blue_geo watch targets test" \
        "blue_geo watch targets upload"; do
        abcli_eval ,$options \
            $module help
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}
