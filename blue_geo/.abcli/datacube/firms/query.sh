#! /usr/bin/env bash

function blue_geo_datacube_firms_area_query() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="dryrun"

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

        abcli_show_usage "@datacube query firms_area$ABCUL[$blue_geo_datacube_query_options]$ABCUL[-|<object-name>]$ABCUL[$options]$ABCUL$args" \
            "firms_area -query-> <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local object_name=$(abcli_clarify_object $2 -)

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.datacube.firms.area \
        query \
        --object_name $object_name \
        "${@:3}"

    return 0
}
