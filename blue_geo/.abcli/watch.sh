#! /usr/bin/env bash

function blue_geo_watch() {
    local options=$1
    local target_options=$2
    local workflow_options=$3
    local processing_options=$4

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local list_of_targets=$(blue_geo_watch_get list_of_targets --delim \|)

        options="$(xtra dryrun)"

        target_options="$(xtra '<query-object-name>,')target=$list_of_targets"

        workflow_options="$(xtra dryrun,)to=$NBS_RUNNERS_LIST"

        processing_options="$(xtra dryrun,~gif)"

        abcli_show_usage "@geo watch $(xwrap $options $target_options $workflow_options $processing_options '-|<object-name>')" \
            "watch target -> <object-name>."

        blue_geo_watch_get "$@"
        blue_geo_watch_view "$@"

        return
    fi

    local task
    for task in get view; do
        if [ $(abcli_option_int "$options" $task 0) == 1 ]; then
            blue_geo_watch_$task "${@:2}"
            return
        fi
    done

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local object_name=$(abcli_clarify_object $5 geo-watch-$(abcli_string_timestamp))

    local target=$(abcli_option "$target_options" target)
    local query_object_name
    if [[ -z "$target" ]]; then
        query_object_name=$target_options

        abcli_download - $query_object_name
    else
        local do_dryrun_targetting=$(abcli_option_int "$target_options" dryrun 0)

        query_object_name=$object_name-query-$(abcli_string_timestamp_short)

        local catalog=$(blue_geo_watch_get catalog --target_name $target)
        local collection=$(blue_geo_watch_get collection --target_name $target)
        local args=$(blue_geo_watch_get args --target_name $target --delim space)

        abcli_eval dryrun=$do_dryrun \
            blue_geo_catalog query $catalog \
            dryrun=$do_dryrun_targetting,$collection \
            - \
            $query_object_name \
            --count -1 \
            $args
    fi

    local job_name="$object_name-job-$(abcli_string_timestamp_short)"

    abcli_log "🌐 @geo: watch: $query_object_name: -[ $workflow_options $processing_options @ $job_name]-> $object_name"

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.watch \
        generate_workflow \
        --query_object_name $query_object_name \
        --job_name $job_name \
        --object_name $object_name \
        --processing_options "$processing_options" \
        "${@:6}"
    [[ $? -ne 0 ]] && return 1

    abcli_eval dryrun=$do_dryrun \
        workflow submit \
        ~download,$workflow_options \
        $job_name
}

abcli_source_path - caller,suffix=/watch
