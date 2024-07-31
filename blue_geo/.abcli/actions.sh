#! /usr/bin/env bash

function blue_geo_action_git_before_push() {
    blue_geo build_README

    [[ "$(abcli_git get_branch)" == "main" ]] &&
        blue_geo pypi build
}
