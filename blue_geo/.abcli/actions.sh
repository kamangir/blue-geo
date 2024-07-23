#! /usr/bin/env bash

function blue_geo_action_git_before_push() {
    if [[ "$(abcli_git get_branch)" == "main" ]]; then
        blue_geo build_README
        blue_geo pypi build
    fi
}
