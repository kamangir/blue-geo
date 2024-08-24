#! /usr/bin/env bash

function blue_geo_watch() {
    local options=$1
    local target_options=$2
    local workflow_options=$3
    local process_options=$4

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local list_of_targets=$(python3 -m blue_geo.watch list \
            --what targets \
            --delim \| \
            --log 0)

        options="$(xtra dryrun,)frames=<frames>,radius=<radius_degree>"

        target_options="$(xtra 'dryrun,datetime=<2024-07-30/2024-08-15>,lat=<51.83>,lon=<-122.78>,')target=$list_of_targets"

        workflow_options="$(xtra dryrun,)to=$NBS_RUNNERS_LIST"

        process_options="~gif"

        abcli_show_usage "@geo watch $(xwrap $options $target_options $workflow_options $process_options '-|<object-name>')" \
            "watch a target."

        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download 0)
    local frames=$(abcli_option_int "$options" frames 10)
    local radius_degree=$(abcli_option "$options" radius 0.1)

    local object_name=$(abcli_clarify_object $5 geo-watch-$(abcli_string_timestamp))

    local job_name="$object_name-job-$(abcli_string_timestamp_short)"

    abcli_log "🌐 @geo: watch: $target_options @ $frames X @ $radius_degree deg : $process_options -$job_name-> $object_name"

    local do_dryrun_targetting=$(abcli_option_int "$target_options" dryrun 0)

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.watch \
        generate_workflow \
        --dryrun $do_dryrun_targetting \
        --frame_count $frames \
        --radius_degree $radius_degree \
        --job_name $job_name \
        --target_description "$target_options" \
        --process_options "$process_options" \
        --object_name $object_name \
        "${@:6}"
    [[ $? -ne 0 ]] && return 1

    workflow submit \
        ~download,$workflow_options \
        $job_name
}
