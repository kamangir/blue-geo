#! /usr/bin/env bash

function test_blue_geo_thing() {
    local options=$1

    local test_options=$2

    abcli_eval ,$options \
        "echo 📜 blue-geo: test: thing: $test_options: ${@:3}."
}


