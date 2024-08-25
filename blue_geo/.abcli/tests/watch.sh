#! /usr/bin/env bash

function test_blue_geo_watch() {
    local options=$1

    blue_geo_watch \
        - \
        target=test \
        to=local \
        - \
        -
}
