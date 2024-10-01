#! /usr/bin/env bash

function test_blue_geo_watch() {
    local options=$1

    local list_of_targets=$(abcli_option "$options" target Chilcotin-test+Leonardo-test)

    local target
    for target in $(echo $list_of_targets | tr + " "); do
        abcli_log "🎯 $target"

        local object_name=test_blue_geo_watch-$target-$(abcli_string_timestamp)

        blue_geo_watch \
            ,$options \
            target=$target \
            to=local \
            - \
            - \
            $object_name
        [[ $? -ne 0 ]] && return 1

        local public_name=test_blue_geo_watch_v3-$target

        abcli_clone \
            ~download \
            $object_name \
            $public_name
        [[ $? -ne 0 ]] && return 1

        abcli_publish \
            tar \
            $public_name
        [[ $? -ne 0 ]] && return 1

        abcli_publish \
            suffix=.gif \
            $public_name
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
