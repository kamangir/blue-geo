#! /usr/bin/env bash

function test_blue_geo_generic() {
    local options=$1

    abcli_eval ,$options \
        blue_geo build_README
}
