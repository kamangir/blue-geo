#! /usr/bin/env bash

function blue_geo_catalog_query_firms() {
    local options=$1

    blue_geo_catalog_query_generic \
        $options,catalog=firms \
        "${@:2}"
}

abcli_source_path - caller,suffix=/query
