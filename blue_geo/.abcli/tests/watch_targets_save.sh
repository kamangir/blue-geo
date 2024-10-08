#! /usr/bin/env bash

function test_blue_geo_watch_targets_save() {
    local options=$1

    abcli_download - $BLUE_GEO_WATCH_TARGET_LIST

    local target_name
    for target_name in Leonardo all; do
        local object_name="test_blue_geo_watch_targets_save-$target_name-$(abcli_string_timestamp)"

        blue_geo_watch_targets save \
            target=$target_name \
            $object_name

        local object_path=$ABCLI_OBJECT_ROOT/$object_name
        [[ ! -f "$object_path/target/shape.geojson" ]] &&
            return 1

        abcli_hr
    done

    return 0
}
