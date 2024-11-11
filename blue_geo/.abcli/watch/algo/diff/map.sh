#! /usr/bin/env bash

function blue_geo_watch_algo_diff_map() {
    local options=$1
    local algo=$(abcli_option "$options" algo diff)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local depth=$(abcli_option "$options" depth 2)
    local offset=$(abcli_option "$options" offset 0)
    local range=$(abcli_option "$options" range 100)
    local suffix=$(abcli_option "$options" suffix $(abcli_string_timestamp_short))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not do_dryrun))

    local query_object_name=$2

    local offset_int=$(python3 -c "print(int('$offset'))")

    local index
    local index_000
    for ((index = offset_int; index < offset_int + depth; index++)); do
        index_000=$(python3 -c "print(f'{$index:03d}')")
        blue_geo_watch_algo_modality_map \
            ,$options,algo=modality,offset=$index_000,suffix=$suffix-$offset-D,~upload \
            "${@:2}"
        [[ $? -ne 0 ]] && return 1
    done

    local object_name=$query_object_name-$suffix-$offset

    blue_geo_watch_targets copy - \
        $query_object_name \
        $object_name

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.watch.algo.$algo \
        map \
        --query_object_name $query_object_name \
        --suffix $suffix \
        --offset $offset \
        --depth $depth \
        --range $range \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return $status
}
