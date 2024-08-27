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
        $(blue_geo_datacube_get catalog $BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2) \
        copernicus
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_get catalog $BLUE_GEO_TEST_DATACUBE_FIRMS_AREA) \
        firms
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_get catalog $BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP) \
        ukraine_timemap
}

function test_blue_geo_datacube_get_list_of_files() {
    abcli_assert \
        "$(blue_geo_datacube_get list_of_files void)" \
        - empty
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        "$(blue_geo_datacube_get list_of_files datacube-generic)" \
        - empty
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_get list_of_files $BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2) \
        - non-empty
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_get list_of_files $BLUE_GEO_TEST_DATACUBE_FIRMS_AREA) \
        - non-empty
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_get list_of_files $BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP) \
        - non-empty
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

    # no template.
    # abcli_assert \
    #     $(blue_geo_datacube_get template $BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2) \
    #     void
    # [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_get template $BLUE_GEO_TEST_DATACUBE_FIRMS_AREA) \
        $BLUE_GEO_QGIS_TEMPLATE_FIRMS_AREA
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_get template $BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP) \
        $BLUE_GEO_QGIS_TEMPLATE_UKRAINE_TIMEMAP
}
