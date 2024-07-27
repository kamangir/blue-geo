#! /usr/bin/env bash

function ukraine_timemap_ingest() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="~copy_template,dryrun,~upload"
        local open_options="open,~QGIS"
        abcli_show_usage "ukraine_timemap ingest$ABCUL[$options]$ABCUL[-|<object-name>]$ABCUL$open_options" \
            "ingest the latest dataset from https://github.com/bellingcat/ukraine-timemap."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_copy_template=$(abcli_option_int "$options" copy_template 1)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 ukraine-timemap-$(abcli_string_timestamp_short))

    if [[ "$do_copy_template" == 1 ]]; then
        abcli_clone \
            $BLUE_GEO_UKRAINE_TIMEMAP_QGIS_TEMPLATE \
            $object_name \
            ~meta
        rm -v \
            $abcli_object_root/$object_name/ukraine_timemap.*
    fi

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.ukraine_timemap \
        ingest \
        --object_name $object_name \
        "${@:4}"

    abcli_tag set \
        $object_name \
        ukraine_timemap_ingest

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    local open_options=$3
    local do_open=$(abcli_option_int "$open_options" open 0)
    [[ "$do_open" == 1 ]] &&
        abcli_open QGIS,$open_options \
            $object_name

    return 0
}
