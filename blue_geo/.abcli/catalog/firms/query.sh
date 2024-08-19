#! /usr/bin/env bash

function blue_geo_catalog_query_firms() {
    blue_geo_catalog_query_generic \
        catalog=firms,$1 \
        "${@:2}"
}

abcli_source_path - caller,suffix=/query
