#! /usr/bin/env bash

function blue_geo_datacube_browse() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="catalog=<catalog>"
        abcli_show_usage "@datacube browse$ABCUL[$options]$ABCUL<args>" \
            "browse <catalog>."
        return
    fi

    local catalog=$(abcli_option "$options" catalog unknown)

    if [[ ",$blue_geo_datacube_list_of_catalogs," != *",catalog,"* ]]; then
        abcli_log_error "-@datacube: browse: $catalog: catalog not found."
        return 1
    fi

    blue_geo_datacube_${catalog}_browse "${@:2}"
}
