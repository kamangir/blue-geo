#! /usr/bin/env bash

function blue_geo_datacube_browse() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        :
        return
    fi

}
