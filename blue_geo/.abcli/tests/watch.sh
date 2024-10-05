#! /usr/bin/env bash

function test_blue_geo_watch() {
    local options=$1

    local list_of_targets=$(abcli_option "$options" target chilcotin-river-landslide-test+Leonardo-test)
    local do_publish=$(abcli_option_int "$options" publish 1)

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

        [[ "$do_publish" == 0 ]] &&
            continue

        local public_name=test_blue_geo_watch_v4-$target
        abcli_log "publishing $object_name -> $public_name ..."

        abcli_publish \
            as=$public_name,~download,tar \
            $object_name
        [[ $? -ne 0 ]] && return 1

        local object_path=$ABCLI_OBJECT_ROOT/$object_name
        cp -v \
            $object_path/$object_name.gif \
            $object_path/$public_name.gif

        abcli_publish \
            as=$public_name,~download,prefix=$public_name,suffix=.gif \
            $object_name
        [[ $? -ne 0 ]] && return 1

        abcli_hr
    done

    return 0
}
