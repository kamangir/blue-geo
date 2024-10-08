#! /usr/bin/env bash

function blue_geo_action_git_before_push() {
    blue_geo build_README

    blue_geo_watch_targets save \
        target=all \
        $BLUE_GEO_WATCH_TARGET_LIST
    cp -v $ABCLI_OBJECT_ROOT/$BLUE_GEO_WATCH_TARGET_LIST/target/shape.geojson \
        $abcli_path_git/blue-geo/blue_geo/watch/targets.geojson

    [[ "$(abcli_git get_branch)" == "main" ]] &&
        blue_geo pypi build
}
