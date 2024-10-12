#! /usr/bin/env bash

function blue_geo_watch_targets_update_template() {
    local options=$1
    local target_name=$(abcli_option "$options" target chilcotin-river-landslide-test)
    local do_download=$(abcli_option "$options" download 1)
    local do_upload=$(abcli_option "$options" upload 1)

    [[ "$do_download" == 1 ]] &&
        abcli_download - $BLUE_GEO_QGIS_TEMPLATE_WATCH

    local object_name=$(abcli_clarify_object $2 .)

    python3 -m blue_geo.watch.targets save \
        --target_name $target_name \
        --object_name $BLUE_GEO_QGIS_TEMPLATE_WATCH \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $BLUE_GEO_QGIS_TEMPLATE_WATCH

    return $status
}
