#! /usr/bin/env bash

function blue_geo_catalog_browse_firms() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="map_key|area"
        abcli_show_usage "@catalog browse firms$ABCUL[$options]" \
            "browse firms."
        return
    fi

    local do_map_key=$(abcli_option_int "$options" map_key 0)
    local collection=$(abcli_option_choice "$options" area area)

    local url="https://firms.modaps.eosdis.nasa.gov/"
    [[ "$do_map_key" == 1 ]] &&
        url="https://firms.modaps.eosdis.nasa.gov/api/map_key/"
    [[ ! -z "$collection" ]] &&
        url="https://firms.modaps.eosdis.nasa.gov/api/$collection/"

    abcli_browse $url
}
