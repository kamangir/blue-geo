#! /usr/bin/env bash

function test_blue_geo_version() {
    local options=$1

    abcli_eval ,$options \
        "blue_geo version ${@:2}"

    return 0
}


