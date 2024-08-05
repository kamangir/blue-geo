#! /usr/bin/env bash

function blue_geo_catalog_ingest_ukraine_timemap() {
    blue_geo_catalog_ingest_generic \
        ,$1 \
        "$2" \
        $3,catalog=ukraine_timemap \
        "${@:4}"
}
