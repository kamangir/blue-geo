#! /usr/bin/env bash

function blue_geo_catalog_query() {
    local catalog=$1

    if [[ ",$blue_geo_list_of_catalogs," != *",$catalog,"* ]]; then
        local function_name=blue_geo_catalog_query_$catalog
        if [[ $(type -t $function_name) == "function" ]]; then
            $function_name "${@:2}"
            return
        fi

        abcli_log_error "@catalog: query: $catalog: catalog not found."
        return 1
    fi

    local options=$2
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_select=$(abcli_option_int "$options" select 0)
    local do_upload=$(abcli_option_int "$options" upload 0)

    local list_of_datacube_classes=$(blue_geo_catalog list \
        datacube_classes \
        --catalog $catalog \
        --delim , \
        --log 0)
    local default_datacube_class=$(blue_geo_catalog list \
        datacube_classes \
        --catalog $catalog \
        --count 1 \
        --delim , \
        --log 0)

    local datacube_class=$(abcli_option_choice "$options" $list_of_datacube_classes)
    [[ -z "$datacube_class" ]] &&
        datacube_class=$default_datacube_class

    local ingest_options=$3

    local object_name=$(abcli_clarify_object $4 query-$catalog-$datacube_class-$(abcli_string_timestamp))

    local is_STAC=$(blue_geo_catalog_get is_STAC --catalog $catalog)

    local log_suffix="🔎"
    local module_name="blue_geo.catalog.$catalog.$datacube_class"
    local extra_args=""
    if [[ "$is_STAC" == 1 ]]; then
        log_suffix="🌐 STAC"
        module_name="blue_geo.catalog.generic.stac"
        extra_args="--catalog $catalog --collection $datacube_class"
    fi

    abcli_log "$log_suffix query: $catalog/$datacube_class -> $object_name ..."

    abcli_eval dryrun=$do_dryrun \
        python3 -m $module_name \
        query \
        --object_name $object_name \
        $extra_args \
        "${@:5}"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    local do_ingest=$(abcli_option_int "$ingest_options" ingest 0)

    [[ "$do_ingest" == 0 ]] &&
        [[ "$do_select" == 0 ]] &&
        return 0

    local datacube_id=$(blue_geo_catalog_query_read - $object_name)
    if [[ -z "$datacube_id" ]]; then
        abcli_log_error "-@catalog: query: $catalog: $datacube_class: no datacube id found."
        return 1
    fi
    abcli_log "🧊 $datacube_id"

    local status=0
    if [[ "$do_ingest" == 1 ]]; then
        blue_geo_datacube_ingest \
            ,$ingest_options \
            $datacube_id
        status="$?"
    fi

    [[ "$do_select" == 1 ]] &&
        abcli_select $datacube_id

    return $status
}

abcli_source_caller_suffix_path /query
