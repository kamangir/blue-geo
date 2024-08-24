#! /usr/bin/env bash

function blue_geo_watch() {
    local options=$1
    local target_options=$2
    local workflow_options=$3

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local list_of_targets=$(python3 -m blue_geo.watch list \
            --what targets \
            --delim \| \
            --log 0)

        options="$(xtra dryrun,)frames=<frames>$(xtra ,upload)"

        target_options="$(xtra 'dryrun,datetime=<2024-07-30/2024-08-15>,lat=<51.83>,lon=<-122.78>,')target=$list_of_targets"

        workflow_options="$(xtra dryrun,)to=$NBS_RUNNERS_LIST"

        abcli_show_usage "@geo watch $(xwrap $options $target_options $workflow_options '-|<object-name>')" \
            "watch a target."

        return
    fi

    local object_name=$(abcli_clarify_object $4 geo-watch-$(abcli_string_timestamp))

    echo "🪄"
}
