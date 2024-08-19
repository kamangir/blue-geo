#! /usr/bin/env bash

function blue_geo_catalog_query_copernicus() {
    blue_geo_catalog_query_generic \
        catalog=copernicus,$1 \
        "${@:2}"
}

abcli_source_path - caller,suffix=/query
