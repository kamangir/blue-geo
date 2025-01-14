#! /usr/bin/env bash

function test_blue_geo_maxar_open_data() {
    local options=$1

    abcli_eval ,$options \
        blue_geo_maxar_open_data \
        ingest \
        event=Maui-Hawaii-fires-Aug-23,~upload,$options \
        test_blue_geo_maxar_open_data-$(abcli_string_timestamp_short) \
        --verbose 1 \
        "${@:2}"
}
