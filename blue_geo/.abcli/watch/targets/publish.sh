#! /usr/bin/env bash

function blue_geo_watch_targets_publish() {
    local options=$1
    local use_template=$(abcli_option_int "$options" template 0)

    local object_name=$BLUE_GEO_WATCH_TARGET_LIST
    [[ "$use_template" == 1 ]] &&
        object_name=$BLUE_GEO_QGIS_TEMPLATE_WATCH

    abcli_publish \
        tar \
        $object_name
}
