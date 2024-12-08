#! /usr/bin/env bash

function blue_geo_ingest() {
    local options=$1
    local do_upload=$(abcli_option_int "$options" upload 0)
    local version=$(abcli_option "$optioms" version v1)

    local object_name=${2:-void}

    local full_object_name=$object_name-$version

    python3 -m blue_geo.objects ingest \
        --object_name $object_name \
        --version $version \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $full_object_name

    return $status
}
