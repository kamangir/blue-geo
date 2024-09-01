#! /usr/bin/env bash

function test_blue_geo_watch() {
    local options=$1

    blue_geo_watch \
        ,$options \
        target=test \
        to=local \
        - \
        publish \
        test_blue_geo_watch
}
