#! /usr/bin/env bash

function test_blue_geo_datacube_get_catalog() {
    abcli_assert \
        $(blue_geo_datacube_get catalog void) \
        void
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_get catalog datacube-generic) \
        generic
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_get catalog $BLUE_GEO_TEST_DATACUBE_FIRMS_AREA) \
        firms
}

function test_blue_geo_datacube_get_template() {
    abcli_assert \
        $(blue_geo_datacube_get template void) \
        unknown-template
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_get template datacube-generic) \
        unknown-template
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_get template $BLUE_GEO_TEST_DATACUBE_FIRMS_AREA) \
        $BLUE_GEO_FIRMS_AREA_QGIS_TEMPLATE
}
