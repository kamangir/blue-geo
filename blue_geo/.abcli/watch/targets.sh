#! /usr/bin/env bash

function blue_geo_watch_targets() {
    local task=$1
    local options=$2

    if [[ "$task" == "help" ]]; then
        blue_geo_watch_targets cp "$@"

        local args="[--delim space]$ABCUL[--target_name <target>]$ABCUL[--what <catalog|collection|exists|query_args>]"
        abcli_show_usage "@geo watch targets get$ABCUL$args" \
            "get <target> info."

        args="[--catalog <catalog>]$ABCUL[--collection <collection>]$ABCUL[--count <count>]$ABCUL[--delim <space>]"
        abcli_show_usage "@geo watch targets list$ABCUL$args" \
            "list targets."

        args="[--target_name <target>]$ABCUL[--object_name <object-name>]"
        abcli_show_usage "@geo watch targets save$ABCUL$args" \
            "save <target> -> <object-name>."
        return
    fi

    if [[ ",cp,copy," == *",$task,"* ]]; then
        if [ $(abcli_option_int "$options" help 0) == 1 ]; then
            options="-"
            abcli_show_usage "@geo watch targets cp|copy$ABCUL[$options]$ABCUL[..|<object-name-1>]$ABCUL[.|<object-name-2>]" \
                "copy <object-name-1>/target -> <object-name-2>."
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
