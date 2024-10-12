#! /usr/bin/env bash

function blue_geo_watch_targets_save() {
    local options=$1
    local target_name=$(abcli_option "$options" target all)

    local object_name=$(abcli_clarify_object $2 .)

    abcli_clone \
        ~relate \
        $BLUE_GEO_QGIS_TEMPLATE_WATCH \
        $object_name

    python3 -m blue_geo.watch.targets save \
        --target_name $target_name \
        --object_name $object_name \
        "${@:3}"
}
