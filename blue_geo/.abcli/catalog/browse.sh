#! /usr/bin/env bash

function blue_geo_catalog_browse() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage "@catalog browse$ABCUL<catalog>$ABCUL<args>" \
            "browse <catalog>."
        return
    fi

    local catalog=$(abcli_option "$options" $blue_geo_catalog_list firms)

    abcli_log "@catalog: browsing $catalog ..."
    blue_geo_catalog_${catalog}_browse "${@:2}"
}
