#! /usr/bin/env bash

function blue_geo_watch_map() {
    local options=$1

    local algo=$(abcli_option "$options" algo modality)
    local allow_failure=$(abcli_option_int "$options" allow_failure 0)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))

    local query_object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $query_object_name

    abcli_log "🌐 @geo watch map $query_object_name: $options -> @algo"

    abcli_eval - \
        blue_geo_watch_algo_${algo}_map "$@"
    local status="$?"

    if [[ "$status" -ne 0 ]]; then
        [[ "$allow_failure" == 1 ]] && return $status

        abcli_log_warning "status: $status, ignored."
    fi

    return 0
}
