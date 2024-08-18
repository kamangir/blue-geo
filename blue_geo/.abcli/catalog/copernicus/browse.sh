#! /usr/bin/env bash

function blue_geo_catalog_browse_copernicus() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="aws_access|doc==docs"
        abcli_show_usage "@catalog browse copernicus$ABCUL[$options]" \
            "browse copernicus."
        return
    fi

    local do_aws_access=$(abcli_option_int "$options" aws_access)
    local do_doc=$(abcli_option_int "$options" doc 0)
    local do_doc=$(abcli_option_int "$options" docs $do_doc)

    local url="https://dataspace.copernicus.eu/"
    [[ "$do_aws_access" == 1 ]] &&
        url="https://documentation.dataspace.copernicus.eu/APIs/S3.html"
    [[ "$do_doc" == 1 ]] &&
        url="https://documentation.dataspace.copernicus.eu/APIs/STAC.html"

    abcli_browse $url
}
