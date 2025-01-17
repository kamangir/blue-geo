#! /usr/bin/env bash

function test_blue_geo_catalog_query_ingest() {
    local options=$1

    abcli_eval ,$options \
        blue_geo_catalog_query_ingest \
        download,index=1 \
        $BLUE_GEO_TEST_QUERY_OBJECT_PALISADES_MAXAR_TEST \
        scope=rgb
    [[ $? -ne 0 ]] && return 1

    abcli_hr

    abcli_eval ,$options \
        blue_geo_catalog_query_ingest \
        download \
        $BLUE_GEO_TEST_QUERY_OBJECT_PALISADES_MAXAR_TEST \
        scope=rgb
}
