#! /usr/bin/env bash

function blue_geo_maxar_open_data_list() {
    local options=$1
    local event_name=$(abcli_option "$options" event all)

    local suffix=$2

    local url="s3://maxar-opendata/events/"

    [[ "$event_name" != all ]] &&
        url="$url$event_name/ard/"

    [[ ! -z "$suffix" ]] &&
        url="$url$suffix"

    abcli_eval ,$options \
        aws s3 ls --no-sign-request $url

    return 0
}
