#! /usr/bin/env bash

function blue_geo_watch_targets_open() {
    local options=$1
    local open_template=$(abcli_option_int "$options" template 0)

    local object_name=$BLUE_GEO_WATCH_TARGET_LIST
    [[ "$open_template" == 1 ]] &&
        object_name=$BLUE_GEO_QGIS_TEMPLATE_WATCH

    abcli_open \
        QGIS,$options \
        $object_name
}
