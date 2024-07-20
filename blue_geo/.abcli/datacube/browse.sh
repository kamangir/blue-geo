#! /usr/bin/env bash

function blue_geo_datacube_browse() {
    local catalog=${1:firms_area}

    if [ $(abcli_option_int "$catalog" help 0) == 1 ]; then
        abcli_show_usage "@datacube browse$ABCUL<catalog>$ABCUL<args>" \
            "browse <catalog>."
        return
    fi

    if [[ ",$blue_geo_datacube_list_of_catalogs," != *",$catalog,"* ]]; then
        abcli_log_error "-@datacube: browse: $catalog: catalog not found."
        return 1
    fi

    blue_geo_datacube_${catalog}_browse "${@:2}"
}
