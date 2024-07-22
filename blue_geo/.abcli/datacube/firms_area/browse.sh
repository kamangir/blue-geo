#! /usr/bin/env bash

function blue_geo_datacube_firms_area_browse() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="|map_key|api"
        abcli_show_usage "@datacube browse firms_area$ABCUL$options" \
            "browse firms_area datacubes."
        return
    fi

    local do_map_key=$(abcli_option_int "$options" map_key 0)
    local do_area_api=$(abcli_option_int "$options" api 0)

    local url="https://firms.modaps.eosdis.nasa.gov/"
    [[ "$do_map_key" == 1 ]] &&
        url="https://firms.modaps.eosdis.nasa.gov/api/map_key/"
    [[ "$do_area_api" == 1 ]] &&
        url="https://firms.modaps.eosdis.nasa.gov/api/area/"

    abcli_browse $url
}
