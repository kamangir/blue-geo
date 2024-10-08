#! /usr/bin/env bash

function blue_geo_watch() {
    local options=$1
    local target_options=$2
    local workflow_options=$3
    local map_options=$4
    local reduce_options=$5

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage_2 blue_geo watch
        return
    fi

    local task
    for task in map reduce targets; do
        if [ $(abcli_option_int "$options" $task 0) == 1 ]; then
            blue_geo_watch_$task "${@:2}"
            return
        fi
    done

    if [[ $(abcli_option_int "$options" batch 0) == 1 ]]; then
        if [ $(abcli_option_int "$target_options" help 0) == 1 ]; then
            abcli_show_usage_2 blue_geo watch batch
            return
        fi

        abcli_aws_batch_eval \
            name=blue-geo-watch-$(abcli_string_timestamp_short),$options,~batch \
            blue_geo_watch \
            - \
            "${@:2}"
        return
    fi

    blue_geo_watch_targets download

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local object_name=$(abcli_clarify_object $6 geo-watch-$(abcli_string_timestamp))

    local target=$(abcli_option "$target_options" target)
    local query_object_name
    if [[ -z "$target" ]]; then
        query_object_name=$target_options

        abcli_download - $query_object_name
    else
        local target_exists=$(blue_geo_watch_targets get \
            --what exists \
            --target_name $target \
            --log 0)
        if [[ "$target_exists" != 1 ]]; then
            abcli_log_error "@geo: watch: $target: target not found."
            return 1
        fi

        local do_dryrun_targetting=$(abcli_option_int "$target_options" dryrun 0)

        query_object_name=$object_name-query-$(abcli_string_timestamp_short)

        local catalog=$(blue_geo_watch_targets get \
            --what catalog \
            --target_name $target \
            --log 0)
        local collection=$(blue_geo_watch_targets get \
            --what collection \
            --target_name $target \
            --log 0)
        local query_args=$(blue_geo_watch_targets get \
            --what query_args \
            --target_name $target \
            --delim space \
            --log 0)

        abcli_eval dryrun=$do_dryrun \
            blue_geo_catalog query $catalog \
            dryrun=$do_dryrun_targetting,$collection \
            - \
            $query_object_name \
            --count -1 \
            $query_args
        [[ $? -ne 0 ]] && return 1

        blue_geo_watch_targets save \
            target=$target \
            $query_object_name
        [[ $? -ne 0 ]] && return 1
    fi

    abcli_upload - $query_object_name

    local job_name="$object_name-job-$(abcli_string_timestamp_short)"

    abcli_log "🌐 @geo: watch: $query_object_name: -[ $workflow_options @ $map_options + $reduce_options @ $job_name]-> $object_name"

    abcli_clone \
        upload \
        $BLUE_GEO_QGIS_TEMPLATE_WATCH \
        $object_name

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
