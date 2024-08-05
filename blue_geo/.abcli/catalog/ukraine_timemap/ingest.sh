#! /usr/bin/env bash

function blue_geo_catalog_ingest_ukraine_timemap() {
    local ingest_options=$1
    local options=$2

    blue_geo_catalog_ingest_generic \
        ,$ingest_options \
        $options,catalog=ukraine_timemap \
        "${@:3}"
}
