#! /usr/bin/env bash

function blue_geo_watch_targets() {
    local task=$1

    if [[ "$task" == "help" ]]; then
        blue_geo_watch_targets cp "$@"
        return
    fi

    if [[ ",cp,copy," == *",$task,"* ]]; then
        local options=$2

        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            local options="$(xtra -)"
            abcli_show_usage "@geo watch targets $(xwrap 'cp|copy' $options '..|<object-name-1>' '.|<object-name-2>')" \
                "copy target <object-name-1> -> <object-name-2>."
            return
        fi

        local object_name_1=$(abcli_clarify_object $3 .)
        local object_name_2=$(abcli_clarify_object $4 .)

        local target_path=$abcli_object_root/$object_name_2/target/
        mkdir -pv $target_path
        cp -v \
            $abcli_object_root/$object_name_1/target/* \
            $target_path

        return
    fi

    python3 -m blue_geo.watch.targets "$@"
}
