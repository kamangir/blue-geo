#! /usr/bin/env bash

function test_@geo_help() {
    # TODO: enable
    return 0

    local options=$1

    local module
    for module in \
        "@geo" \
        \
        "@geo pytest" \
        \
        "@geo catalog" \
        "@geo catalog browse" \
        "@geo catalog get" \
        "@geo catalog list" \
        "@geo catalog query" \
        \
        "@geo datacube" \
        "@geo datacube crop" \
        "@geo datacube generate" \
        "@geo datacube get" \
        "@geo datacube ingest" \
        "@geo datacube list" \
        \
        "@geo gdal" \
        \
        "QGIS" \
        "QGIS expressions" \
        "QGIS expressions pull" \
        "QGIS expressions push" \
        "QGIS server" \
        \
        "@geo watch" \
        "@geo watch batch" \
        "@geo watch map" \
        "@geo watch reduce" \
        \
        "@geo watch targets" \
        "@geo watch targets cat" \
        "@geo watch targets cp" \
        "@geo watch targets copy" \
        "@geo watch targets download" \
        "@geo watch targets edit" \
        "@geo watch targets get" \
        "@geo watch targets list" \
        "@geo watch targets open" \
        "@geo watch targets publish" \
        "@geo watch targets save" \
        "@geo watch targets test" \
        "@geo watch targets update_template" \
        "@geo watch targets upload"; do
        abcli_eval ,$options \
            abcli_help $module
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
