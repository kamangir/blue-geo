#! /usr/bin/env bash

export blue_geo_catalog_query_options="download,ingest,select,upload"

function blue_geo_catalog_query() {
    local catalog=${1:firms}

    local options=$2

    if [ $(abcli_option_int "$catalog" help 0) == 1 ]; then
        for catalog in $(echo $blue_geo_catalog_list | tr , " "); do
            blue_geo_catalog_query_${catalog} "$@"
        done

        blue_geo_catalog_query_read "$@"
        return
    fi

    local do_download=$(abcli_option_int "$options" download 0)
    local do_ingest=$(abcli_option_int "$options" ingest 0)
    local do_select=$(abcli_option_int "$options" select 0)
    local do_upload=$(abcli_option_int "$options" upload 0)

    if [[ ",$blue_geo_catalog_list," != *",$catalog,"* ]]; then
        local function_name=blue_geo_catalog_query_$catalog
        if [[ $(type -t $function_name) == "function" ]]; then
            $function_name "${@:2}"
            return
        fi

        abcli_log_error "-@catalog: query: $catalog: catalog not found."
        return 1
    fi

    if [[ $(abcli_option_int "$options" help 0) == 1 ]]; then
        blue_geo_catalog_query_${catalog} "${@:2}"
        return
    fi

    local object_name=$(abcli_clarify_object $3 query-$catalog-$(abcli_string_timestamp))

    local query_options=$4

    abcli_log "🌐 query: $catalog -$query_options-> $object_name"

    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    blue_geo_catalog_query_${catalog} \
        ,$query_options \
        $object_name \
        "${@:5}"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    [[ "$do_ingest" == 0 ]] && [[ "$do_select" == 0 ]] &&
        return 0

    local datacube_id=$(blue_geo_catalog_query_read - $object_name)
    if [[ -z "$datacube_id" ]]; then
        abcli_log_error "-@catalog: query: $catalog: no datacube id found."
        return 1
    fi
    abcli_log "🧊 $datacube_id"

    [[ "$do_ingest" == 1 ]] &&
        blue_geo_datacube_ingest - $datacube_id

    [[ "$do_select" == 1 ]] &&
        abcli_select $datacube_id

    return 0

}

abcli_source_path - caller,suffix=/query
