#! /usr/bin/env bash

function blue_geo_action_git_before_push() {
    blue_geo build_README
    [[ $? -ne 0 ]] && return 1

    [[ "$(abcli_git get_branch)" != "main" ]] &&
        return 0

    blue_geo_watch_targets_upload
    [[ $? -ne 0 ]] && return 1

    cp -v $ABCLI_OBJECT_ROOT/$BLUE_GEO_WATCH_TARGET_LIST/target/shape.geojson \
        $abcli_path_git/blue-geo/blue_geo/watch/targets.geojson
    [[ $? -ne 0 ]] && return 1

    blue_geo pypi build
}
