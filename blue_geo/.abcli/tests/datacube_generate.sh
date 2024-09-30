#! /usr/bin/env bash

function test_blue_geo_datacube_generate() {
    local options=$1

    local datacube_id=$BLUE_GEO_TEST_DATACUBE_SKYFOX_VENUS

    blue_geo_datacube_ingest \
        scope=rgbx,$options \
        $datacube_id

    blue_geo_datacube_generate \
        ,$options \
        $datacube_id \
        --modality rgb
}
