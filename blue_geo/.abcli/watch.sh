#! /usr/bin/env bash

function blue_geo_watch() {
    local options=$1
    local target_options=$2
    local workflow_options=$3
    local map_options=$4
    local reduce_options=$5

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local list_of_targets=$(python3 -m blue_geo.watch.targets get \
            --what list \
            --delim \|)

        options="$(xtra dryrun)"

        target_options="$(xtra '<query-object-name>,')target=$list_of_targets"

        workflow_options="$(xtra dryrun,)to=$NBS_RUNNERS_LIST"

        map_options="$(xtra dryrun)"

        reduce_options="$(xtra dryrun,~gif)"

        abcli_show_usage "@geo watch $(xwrap $options $target_options $workflow_options $map_options $reduce_options '-|<object-name>')" \
            "watch target -> <object-name>."

        blue_geo_watch_map "$@"
        blue_geo_watch_reduce "$@"

        return
    fi

    local task
    for task in map reduce; do
        if [ $(abcli_option_int "$options" $task 0) == 1 ]; then
            blue_geo_watch_$task "${@:2}"
            return
        fi
    done

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local object_name=$(abcli_clarify_object $6 geo-watch-$(abcli_string_timestamp))

    local target=$(abcli_option "$target_options" target)
    local query_object_name
    if [[ -z "$target" ]]; then
        query_object_name=$target_options

        abcli_download - $query_object_name
    else
        local do_dryrun_targetting=$(abcli_option_int "$target_options" dryrun 0)

        query_object_name=$object_name-query-$(abcli_string_timestamp_short)

        local catalog=$(python3 -m blue_geo.watch.targets get \
            --what catalog \
            --target_name $target)
        local collection=$(python3 -m blue_geo.watch.targets get \
            --what collection \
            --target_name $target)
        local args=$(python3 -m blue_geo.watch.targets get \
            --what args \
            --target_name $target \
            --delim space)

        abcli_eval dryrun=$do_dryrun \
            blue_geo_catalog query $catalog \
            dryrun=$do_dryrun_targetting,$collection \
            - \
            $query_object_name \
            --count -1 \
            $args
    fi

    local job_name="$object_name-job-$(abcli_string_timestamp_short)"

    abcli_log "🌐 @geo: watch: $query_object_name: -[ $workflow_options @ $map_options + $reduce_options @ $job_name]-> $object_name"

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.watch.workflow \
        generate \
        --query_object_name $query_object_name \
        --job_name $job_name \
        --object_name $object_name \
        --map_options "$map_options" \
        --reduce_options "$reduce_options" \
        "${@:7}"
    [[ $? -ne 0 ]] && return 1

    abcli_eval dryrun=$do_dryrun \
        workflow submit \
        ~download,$workflow_options \
        $job_name
}

abcli_source_path - caller,suffix=/watch
