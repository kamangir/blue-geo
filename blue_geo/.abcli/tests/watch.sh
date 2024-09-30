#! /usr/bin/env bash

function test_blue_geo_watch() {
    local options=$1

    local object_name=test_blue_geo_watch-$(abcli_string_timestamp)

    blue_geo_watch \
        ,$options \
        target=test \
        to=local \
        - \
        - \
        $object_name

    abcli_clone \
        ~download \
        $object_name \
        test_blue_geo_watch_v2

    abcli_publish \
        tar \
        test_blue_geo_watch_v2

    abcli_publish \
        suffix=.gif \
        test_blue_geo_watch_v2
}
