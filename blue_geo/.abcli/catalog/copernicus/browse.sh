#! /usr/bin/env bash

function blue_geo_catalog_browse_copernicus() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="doc"
        abcli_show_usage "@catalog browse copernicus$ABCUL[$options]" \
            "browse copernicus."
        return
    fi

    local do_doc=$(abcli_option_int "$options" doc 0)

    local url="https://dataspace.copernicus.eu/"
    [[ "$do_doc" == 1 ]] &&
        url="https://documentation.dataspace.copernicus.eu/APIs/STAC.html"

    abcli_browse $url
}
