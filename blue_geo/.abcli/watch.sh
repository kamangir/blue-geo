#! /usr/bin/env bash

function blue_geo_watch() {
    local options=$1
    local target_options=$2
    local algo_options=$3
    local workflow_options=$4
    local map_options=$5
    local reduce_options=$6

    blue_geo_watch_targets_download

    local task
    for task in map reduce targets query; do
        if [ $(abcli_option_int "$options" $task 0) == 1 ]; then
            blue_geo_watch_$task "${@:2}"
            return
        fi
    done

    if [[ $(abcli_option_int "$options" batch 0) == 1 ]]; then
        abcli_aws_batch_eval \
            name=blue-geo-watch-$(abcli_string_timestamp_short),$options,~batch \
            blue_geo_watch \
            - \
            "${@:2}"
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local algo=$(abcli_option "$algo_options" algo modality)

    local object_name=$(abcli_clarify_object $7 geo-watch-$(abcli_string_timestamp))

    local target=$(abcli_option "$target_options" target)
    local query_object_name
    if [[ -z "$target" ]]; then
        query_object_name=$target_options

        abcli_download - $query_object_name
    else
        query_object_name=$object_name-query-$(abcli_string_timestamp_short)

        blue_geo_watch_query \
            $target_options \
            $query_object_name
        [[ $? -ne 0 ]] && return 1
    fi

    local job_name="$object_name-job-$(abcli_string_timestamp_short)"

    abcli_log "🌐 @geo: watch: $query_object_name: -[ $workflow_options @ $map_options + $reduce_options @ $job_name]-> $object_name"

    abcli_clone \
        upload \
        $BLUE_GEO_QGIS_TEMPLATE_WATCH \
        $object_name

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.watch.workflow \
        generate \
        --algo_options $algo_options \
        --query_object_name $query_object_name \
        --job_name $job_name \
        --object_name $object_name \
        --map_options ",$map_options" \
        --reduce_options ",$reduce_options" \
        "${@:8}"
    [[ $? -ne 0 ]] && return 1

    abcli_eval - \
        blue_geo_watch_algo_${algo}_generate "$@"
    [[ $? -ne 0 ]] && return 1

    local do_submit=$(abcli_option_int "$workflow_options" submit 1)
    [[ "$do_submit" == 0 ]] && return 0

    abcli_eval dryrun=$do_dryrun \
        blueflow_workflow_submit \
        ~download,$workflow_options \
        $job_name
}

abcli_source_caller_suffix_path /watch

abcli_source_caller_suffix_path /watch/algo/diff
abcli_source_caller_suffix_path /watch/algo/modality
