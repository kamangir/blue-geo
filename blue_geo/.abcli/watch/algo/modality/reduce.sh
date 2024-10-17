#! /usr/bin/env bash

function blue_geo_watch_algo_modality_reduce() {
    local options=$1
    local algo=$(abcli_option "$options" algo modality)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local suffix=$(abcli_option "$options" suffix)

    local query_object_name=$(abcli_clarify_object $2 ..)

    local object_name=$(abcli_clarify_object $3 .)

    abcli_log "@geo: watch: algo: $algo: reduce"

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.watch.algo.$algo \
        reduce \
        --query_object_name $query_object_name \
        --suffix $suffix \
        --object_name $object_name \
        "${@:4}"
}
