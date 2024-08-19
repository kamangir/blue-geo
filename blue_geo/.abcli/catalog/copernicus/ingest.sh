#! /usr/bin/env bash

function blue_geo_catalog_ingest_copernicus() {
    blue_geo_catalog_ingest_generic \
        ,$1 \
        "$2" \
        $3,catalog=copernicus \
        "${@:4}"
}
