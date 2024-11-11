#! /usr/bin/env bash

function blue_geo_watch_query() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local target=$(abcli_option "$options" target)
    if [[ -z "$target" ]]; then
        abcli_log_error "target not found."
        return 1
    fi

    local target_exists=$(blue_geo_watch_targets get \
        --what exists \
        --target_name $target \
        --log 0)
    if [[ "$target_exists" != 1 ]]; then
        abcli_log_error "$target: target not found."
        return 1
    fi

    local catalog=$(blue_geo_watch_targets get \
        --what catalog \
        --target_name $target \
        --log 0)
    local collection=$(blue_geo_watch_targets get \
        --what collection \
        --target_name $target \
        --log 0)
    local query_args=$(blue_geo_watch_targets get \
        --what query_args \
        --target_name $target \
        --delim space \
        --log 0)

    local object_name=$(abcli_clarify_object $2 .)

    abcli_log "🎯 $target: $catalog/$collection: $query_args -> $object_name"

    abcli_eval dryrun=$do_dryrun \
        blue_geo_catalog query $catalog \
        $collection \
        - \
        $object_name \
        --count -1 \
        $query_args
    local status="$?"

    blue_geo_watch_targets save \
        target=$target \
        $object_name
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return "$status"
}
