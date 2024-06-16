#! /usr/bin/env bash

function test_blue_plugin_version() {
    local options=$1

    abcli_eval ,$options \
        "blue_plugin version ${@:2}"

    return 0
}
