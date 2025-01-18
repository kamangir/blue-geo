#! /usr/bin/env bash

function test_blue_geo_datacube_label() {
    local datacube_id=$BLUE_GEO_PALISADES_TEST_DATACUBE

    blue_geo_datacube_ingest \
        scope=rgb \
        $datacube_id

    blue_geo_datacube_label ~QGIS \
        $datacube_id
}
