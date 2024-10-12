#! /usr/bin/env bash

function test_blue_geo_watch_targets_cp() {
    local object_1_name="test_blue_geo_watch_targets_cp-$(abcli_string_timestamp)"
    local object_2_name="test_blue_geo_watch_targets_cp-$(abcli_string_timestamp)"

    blue_geo_watch_targets save \
        target=chilcotin-river-landslide-test \
        $object_1_name
    [[ $? -ne 0 ]] && return 1

    blue_geo_watch_targets cp - \
        $object_1_name \
        $object_2_name
    [[ $? -ne 0 ]] && return 1

    abcli_assert_file_exists \
        $ABCLI_OBJECT_ROOT/$object_2_name/target/shape.geojson
}
