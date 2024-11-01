#! /usr/bin/env bash

function blue_geo_catalog_get() {
    python3 -m blue_geo.catalog \
        get \
        --what "$1" \
        "${@:2}"
}
