#! /usr/bin/env bash

function test_blue_geo_datacube_crop() {
    local options=$1

    local datacube_id=$BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2_CHILCOTIN
    blue_geo_datacube_ingest \
        scope=rgbx,$options \
        $datacube_id

    local suffix=test_blue_geo_datacube_crop-$(abcli_string_timestamp_short)

    blue_geo_datacube_crop \
        suffix=$suffix,$options \
        $BLUE_GEO_TEST_DATACUBE_CROP_CTULINE \
        $datacube_id
}
