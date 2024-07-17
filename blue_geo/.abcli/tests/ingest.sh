#! /usr/bin/env bash

function test_blue_geo_ingest() {
    local object_name=ingest-$(abcli_string_timestamp_short)

    abcli_eval dryrun=$do_dryrun \
        blue_geo ingest firms - \
        $object_name \
        "${@:2}"
}
