#! /usr/bin/env bash

function test_blue_geo_datacube_list() {
    local datacube_id

    for datacube_id in \
        void \
        datacube-generic; do
        abcli_assert \
            "$(blue_geo_datacube_list $datacube_id --log 0)" \
            - empty
        [[ $? -ne 0 ]] && return 1
    done

    for datacube_id in \
        $BLUE_GEO_TEST_DATACUBE_COPERNICUS_SENTINEL_2 \
        $BLUE_GEO_TEST_DATACUBE_EARTHSEARCH_SENTINEL2_L1C \
        $BLUE_GEO_TEST_DATACUBE_FIRMS_AREA \
        $BLUE_GEO_TEST_DATACUBE_SKYFOX_VENUS \
        $BLUE_GEO_TEST_DATACUBE_UKRAINE_TIMEMAP; do
        abcli_assert \
            $(blue_geo_datacube_list $datacube_id --log 0) \
            - non-empty
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}
