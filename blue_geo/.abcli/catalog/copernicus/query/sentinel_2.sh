#! /usr/bin/env bash

function blue_geo_catalog_query_copernicus_sentinel_2() {
    blue_geo_catalog_query_generic_generic \
        catalog=copernicus,datacube_class=sentinel_2,$1 \
        "${@:2}"
}
