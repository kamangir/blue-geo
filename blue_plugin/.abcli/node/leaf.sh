#! /usr/bin/env bash

function blue_plugin_node_leaf() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="~download,dryrun,~upload"
        local args="[--<keyword-1> <value>]$ABCUL[--<keyword-2> <value>]"
        abcli_show_usage "blue_plugin node leaf$ABCUL[$options]$ABCUL[.|<object-name-1>]$ABCUL[-|<object-name-2>]$ABCUL$args" \
            "<object-name-1> -[blue-plugin node leaf]-> <object-name-2>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name_1=$(abcli_clarify_object $3 .)

    [[ "$do_dryrun" == 1 ]] &&
        abcli_download - $object_name_1

    local object_name_2=$(abcli_clarify_object $4 $(abcli_string_timestamp))

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_plugin.node \
        leaf \
        --object_name_1 $object_name_1 \
        --object_name_2 $object_name_2 \
        "${@:4}"

    [[ "$do_dryrun" == 1 ]] &&
        abcli_upload - $object_name_2
}
