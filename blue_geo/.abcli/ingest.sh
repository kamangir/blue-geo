#! /usr/bin/env bash

function blue_geo_ingest() {
    local options=$1
    local do_publish=$(abcli_option_int "$options" publish 0)
    local do_upload=$(abcli_option_int "$options" upload 0)

    local object_name=${2:-void}

    local version=$(python3 -m blue_geo.objects get \
        --what version \
        --object_name $object_name)
    version=$(abcli_option "$options" version $version)

    local full_object_name=$object_name-$version

    local template_object_name=$(python3 -m blue_geo.objects get \
        --what template_name \
        --object_name $object_name)
    [[ ! -z "$template_object_name" ]] &&
        abcli_clone \
            - \
            $template_object_name \
            $full_object_name

    abcli_log "ingesting $full_object_name ..."

    python3 -m blue_geo.objects ingest \
        --object_name $object_name \
        --version $version \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $full_object_name

    [[ "$do_publish" == 1 ]] &&
        abcli_publish \
            ~download,tar \
            $full_object_name

    return $status
}
