#! /usr/bin/env bash

function blue_geo_log() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload 0)
    local filename=$(abcli_option "$options" filename void)

    local object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    abcli_eval do_dryrun=$do_dryrun \
        python3 -m blue_geo.logger log_geoimage \
        --object_name $object_name \
        --filename $filename \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return $status
}
