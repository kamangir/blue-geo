#! /usr/bin/env bash

function blue_geo_catalog_query_ingest() {
    local options=$1
    local do_download=$(abcli_option_int "$options" download 0)

    local query_object_name=$(abcli_clarify_object $2 .)

    local datacube_ingest_options=$3

    [[ "$do_download" == 1 ]] &&
        abcli_download - $query_object_name

    local list_of_datacubes=$(blue_geo_catalog_query_read all \
        $query_object_name \
        --log 0 \
        --delim +)

    abcli_log_list "$list_of_datacubes" \
        --before ingesting \
        --after "datacube(s)" \
        --delim +

    local datacube_id
    for datacube_id in $(echo $list_of_datacubes | tr + " "); do
        blue_geo_datacube_ingest \
            ,$datacube_ingest_options \
            $datacube_id
        [[ $? -ne 0 ]] && return 1
    done

    return 0
}
