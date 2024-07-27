#! /usr/bin/env bash

export blue_geo_datacube_ingest_options="assets=all|<item-1+item-2>,~copy_template,dryrun,suffix=<suffix>,upload"

function blue_geo_datacube_ingest() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options=$blue_geo_datacube_ingest_options
        abcli_show_usage "@datacube ingest$ABCUL[$options]$ABCUL[.|<object-name>]$ABCUL[<args>]" \
            "ingest <object-name>."
        return
    fi

    local do_upload=$(abcli_option_int "$options" upload 0)

    local object_name=$(abcli_clarify_object $2 .)

    local catalog=$(blue_geo_datacube get catalog $object_name)
    if [[ "$catalog" == "void" ]]; then
        abcli_log_error "-@datacube: ingest: $object_name: catalog not found."
        return 1
    fi

    abcli_log "🧊 catalog: $catalog"

    local template_object_name=$(blue_geo_datacube get template $object_name)
    local do_copy_template=1
    [[ "$template_object_name" == "unknown-template" ]] &&
        do_copy_template=0
    do_copy_template=$(abcli_option_int "$options" copy_template $do_copy_template)

    [[ "$do_copy_template" == 1 ]] &&
        abcli_clone \
            $template_object_name \
            $object_name \
            ~meta

    blue_geo_catalog_ingest_${catalog} "$@"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return 0
}
