#! /usr/bin/env bash

function test_blue_geo_gdal_get_crs() {
    local options=$1

    local object_name=$BLUE_GEO_WATCH_TARGET_LIST
    abcli_download - $object_name

    local crs=$(blue_geo_gdal_get_crs $ABCLI_OBJECT_ROOT/$object_name/target/shape.geojson)

    abcli_assert "$crs" EPSG:4326
}
