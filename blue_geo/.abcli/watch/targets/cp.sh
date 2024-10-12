#! /usr/bin/env bash

function blue_geo_watch_targets_cp() {
    local options=$1

    local object_name_1=$(abcli_clarify_object $2 .)
    local object_name_2=$(abcli_clarify_object $3 .)

    local target_path=$ABCLI_OBJECT_ROOT/$object_name_2/target/
    mkdir -pv $target_path
    cp -v \
        $ABCLI_OBJECT_ROOT/$object_name_1/target/* \
        $target_path
    # because there may be no such ^ file, and its ok. :)
    return 0
}
