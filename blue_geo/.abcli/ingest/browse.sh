#! /usr/bin/env bash

function firms_browse() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="home$EOP|map_key|area-api$EOPE"
        abcli_show_usage "firms browse$ABCUL$options" \
            "browse firms."
        return
    fi

    local do_map_key=$(abcli_option_int "$options" map_key 0)
    local do_area_api=$(abcli_option_int "$options" area-api 0)

    local url="https://firms.modaps.eosdis.nasa.gov/"
    [[ "$do_map_key" == 1 ]] &&
        url="https://firms.modaps.eosdis.nasa.gov/api/map_key/"
    [[ "$do_area_api" == 1 ]] &&
        url="https://firms.modaps.eosdis.nasa.gov/api/area/"

    abcli_browse $url
}
