#! /usr/bin/env bash

function test_blue_geo_datacube_get_catalog() {
    abcli_assert \
        $(blue_geo_datacube_get catalog void) \
        unknown-catalog

    abcli_assert \
        $(blue_geo_datacube_get catalog datacube-generic) \
        generic

    abcli_assert \
        $(blue_geo_datacube_get catalog datacube-firms_area-world-MODIS_NRT-2024-07-20-1) \
        firms_area
}

function test_blue_geo_datacube_get_template() {
    abcli_assert \
        $(blue_geo_datacube_get template unknown-catalog) \
        unknown-template

    abcli_assert \
        $(blue_geo_datacube_get template generic) \
        unknown-template

    abcli_assert \
        $(blue_geo_datacube_get template firms_area) \
        $BLUE_GEO_FIRMS_AREA_QGIS_TEMPLATE
}
