#! /usr/bin/env bash

function test_blue_geo_maxar_open_data_list() {
    local options=$1

    abcli_eval ,$options \
        blue_geo_maxar_open_data \
        list
}
