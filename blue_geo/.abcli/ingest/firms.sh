#! /usr/bin/env bash

function blue_geo_ingest_firms() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="$EOP~copy_template,dryrun,~upload$EOPE"
        local date=$(abcli_string_timestamp_short \
            --include_time 0 \
            --unique 0)
        local area=$(python3 -m blue_geo.datacube.firms.area \
            get \
            --what area \
            --delim \|)
        local source=$(python3 -m blue_geo.datacube.firms.area \
            get \
            --what source \
            --values 1 \
            --delim \|)
        local args="[--date $date]$ABCUL[--depth 1]$ABCUL[--area $area]$ABCUL[--source $source]$ABCUL[--log 1]"
        abcli_show_usage "blue_geo ingest firms$ABCUL[$options]$ABCUL[.|<object-name>]$ABCUL$args" \
            "firms -ingest-> <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_copy_template=$(abcli_option_int "$options" copy_template 1)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 .)

    if [[ "$do_copy_template" == 1 ]]; then
        abcli_clone \
            $BLUE_GEO_FIRMS_QGIS_TEMPLATE \
            $object_name \
            ~meta
        rm -v \
            $abcli_object_root/$object_name/firms.*
    fi

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.datacube.firms.area \
        ingest \
        --object_name $object_name \
        "${@:4}"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return 0
}
