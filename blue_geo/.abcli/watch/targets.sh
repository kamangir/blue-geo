#! /usr/bin/env bash

function blue_geo_watch_targets() {
    local task=$1
    local options=$2

    if [[ "$task" == "help" ]]; then
        abcli_show_usage_2 blue_geo watch targets
        return
    fi

    if [[ ",cp,copy," == *",$task,"* ]]; then
        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            abcli_show_usage_2 blue_geo watch targets cp
            return
        fi

        local object_name_1=$(abcli_clarify_object $3 .)
        local object_name_2=$(abcli_clarify_object $4 .)

        local target_path=$ABCLI_OBJECT_ROOT/$object_name_2/target/
        mkdir -pv $target_path
        cp -v \
            $ABCLI_OBJECT_ROOT/$object_name_1/target/* \
            $target_path

        return
    fi

    python3 -m blue_geo.watch.targets "$@"
}
