#! /usr/bin/env bash

function blue_geo_catalog_query_ukraine_timemap_ukraine_timemap() {
    blue_geo_catalog_query_generic_generic \
        catalog=ukraine_timemap,datacube_class=ukraine_timemap,$1 \
        "${@:2}"
}
