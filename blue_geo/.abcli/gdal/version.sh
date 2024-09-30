#! /usr/bin/env bash

function blue_geo_gdal_version() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage_2 blue_geo gdal version
        return
    fi

    gdalinfo --version
}
