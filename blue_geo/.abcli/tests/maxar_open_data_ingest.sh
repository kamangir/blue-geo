#! /usr/bin/env bash

function test_blue_geo_maxar_open_data_ingest() {
    local options=$1

    abcli_eval ,$options \
        blue_geo_maxar_open_data \
        ingest \
        ~upload,$options \
        $BLUE_GEO_TEST_DATACUBE_MAXAR_OPEN_DATA \
        --verbose 1 \
        "${@:2}"
}
