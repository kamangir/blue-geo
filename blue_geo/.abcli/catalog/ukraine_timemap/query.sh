#! /usr/bin/env bash

function blue_geo_catalog_query_ukraine_timemap() {
    blue_geo_catalog_query_generic \
        catalog=ukraine_timemap,$1 \
        "${@:2}"
}

abcli_source_path - caller,suffix=/query
