#! /usr/bin/env bash

function test_blue_geo_firms() {
    local options=$1

    local object_name=firms-$(abcli_string_timestamp_short)

    blue_geo ingest firms $options, $object_name
}
