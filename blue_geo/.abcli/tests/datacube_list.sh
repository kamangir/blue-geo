#! /usr/bin/env bash

function test_blue_geo_datacube_list() {
    abcli_assert \
        "$(blue_geo_datacube_list void --log 0)" \
        - empty
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        "$(blue_geo_datacube_list datacube-generic --log 0)" \
        - empty
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_list $BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2 --log 0) \
        - non-empty
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_list $BLUE_GEO_TEST_DATACUBE_FIRMS_AREA --log 0) \
        - non-empty
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_datacube_list $BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP --log 0) \
        - non-empty
}
