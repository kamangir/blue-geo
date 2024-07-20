#! /usr/bin/env bash

export blue_geo_datacube_query_read_args="[--index <index>]$ABCUL[--prefix <prefix>]$ABCUL[--suffix <suffix>]$ABCUL[--contains <contains>]$ABCUL[--notcontains <not-contains>]"

function blue_geo_datacube_query() {
    local catalog=${1:firms_area}

    local options=$2

    if [ $(abcli_option_int "$catalog" help 0) == 1 ]; then
        options="download,ingest,select,upload"
        abcli_show_usage "@datacube query$ABCUL<catalog>$ABCUL$options$ABCUL-|<object-name>$ABCUL<args>" \
            "query <catalog>."

        blue_geo_datacube_query_len "$@"
        blue_geo_datacube_query_read "$@"
        return
    fi

    local function_name=blue_geo_datacube_query_$catalog
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    local do_download=$(abcli_option_int "$options" download 0)
    local do_ingest=$(abcli_option_int "$options" ingest 0)
    local do_select=$(abcli_option_int "$options" select 0)
    local do_upload=$(abcli_option_int "$options" upload 0)

    local object_name=$(abcli_clarify_object $3 query-$catalog-$(abcli_string_timestamp))

    if [[ ",$blue_geo_datacube_list_of_catalogs," != *",$catalog,"* ]]; then
        abcli_log_error "-@datacube: query: $catalog: catalog not found."
        return 1
    fi

    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    blue_geo_datacube_${catalog}_query \
        $object_name \
        "${@:4}"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    [[ "$do_ingest" == 0 ]] && [[ "$do_select" == 0 ]] &&
        return 0

    local datacube_id=$(blue_geo_datacube_query_read - $object_name)
    abcli_log "🧊 $datacube_id"

    [[ "$do_ingest" == 1 ]] &&
        blue_geo_datacube_ingest - $datacube_id

    [[ "$do_select" == 1 ]] &&
        abcli_select - $datacube_id

    return 0

}

abcli_source_path - caller,suffix=/query
