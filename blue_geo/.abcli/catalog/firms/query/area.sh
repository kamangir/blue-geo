#! /usr/bin/env bash

function blue_geo_catalog_query_firms_area() {
    blue_geo_catalog_query_generic_generic \
        catalog=firms,datacube_class=area,$1 \
        "${@:2}"
}
