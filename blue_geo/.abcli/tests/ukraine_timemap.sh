#! /usr/bin/env bash

function test_blue_geo_ukraine_timemap() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload 0)

    local object_name=ukraine-timemap-$(abcli_string_timestamp_short)

    abcli_eval dryrun=$do_dryrun \
        ukraine_timemap ingest \
        upload=$do_upload,$2 \
        $object_name \
        "${@:3}"
    [[ $? -ne 0 ]] && return 1

    abcli_publish \
        as=ukraine_timemap,tar \
        $object_name
    [[ $? -ne 0 ]] && return 1

    abcli_publish \
        as=ukraine_timemap,suffix=.png \
        $object_name
}
