#! /usr/bin/env bash

function test_blue_geo_maxar_open_data_list() {
    local options=$1

    abcli_eval ,$options \
        blue_geo_maxar_open_data \
        list
    [[ $? -ne 0 ]] && return 1

    abcli_eval ,$options \
        blue_geo_maxar_open_data \
        list \
        event=Maui-Hawaii-fires-Aug-23
    [[ $? -ne 0 ]] && return 1

    abcli_eval ,$options \
        blue_geo_maxar_open_data \
        list \
        event=Maui-Hawaii-fires-Aug-23 \
        04/
}
