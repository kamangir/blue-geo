#! /usr/bin/env bash

function blue_geo_watch() {
    local options=$1
    local workflow_options=$2

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local list_of_targets=$(python3 -m blue_geo.watch list \
            --log 0 \
            --what targets \
            --delim \|)
        options="dryrun,upload"
        target_options="target=$list_of_targets$EOP,datetime=<2024-07-30/2024-08-15>,lat=<51.83>,lon=<-122.78>$EOPE"
        workflow_options="${EOP}dryrun,${EOPE}to=$NBS_RUNNERS_LIST"
        abcli_show_usage "@geo watch$ABCUL[$options]$ABCUL[$target_options]$ABCUL[$workflow_options]$ABCUL[-|<object-name>]" \
            "watch a target."
        return
    fi

    local object_name=$(abcli_clarify_object $3 watching-$target-$(abcli_string_timestamp))

    echo "🪄"
}
