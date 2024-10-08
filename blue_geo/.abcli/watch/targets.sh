#! /usr/bin/env bash

function blue_geo_watch_targets() {
    local task=$1
    [[ "$task" == "copy" ]] && task="cp"

    if [[ "$task" == "help" ]]; then
        abcli_show_usage_2 blue_geo watch targets
        return
    fi

    local function_name=blue_geo_watch_targets_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [ "$2" == "help" ]; then
        abcli_show_usage_2 blue_geo watch targets $task
        return
    fi

    if [[ "$task" == "cat" ]]; then
        local target_name=$2
        if [[ -z "$target_name" ]]; then
            abcli_log_error "-@targets cat: <target-name> not found."
            return 1
        fi

        python3 -m blue_geo.watch.targets \
            get \
            --target_name $target_name \
            --what one_liner
        return
    fi

    if [[ "$task" == "download" ]]; then
        abcli_$task - $BLUE_GEO_WATCH_TARGET_LIST

        python3 -m blue_geo.watch.targets list
        return
    fi

    if [[ "$task" == "edit" ]]; then
        abcli_eval - \
            nano $ABCLI_OBJECT_ROOT/$BLUE_GEO_WATCH_TARGET_LIST/metadata.yaml
        return
    fi

    if [[ ",get,list," == *","$task","* ]]; then
        python3 -m blue_geo.watch.targets "$@"
        return
    fi

    if [[ "$task" == "save" ]]; then
        local options=$2
        local target_name=$(abcli_option "$options" target all)

        local object_name=$(abcli_clarify_object $3 .)

        abcli_clone \
            ~relate \
            $BLUE_GEO_QGIS_TEMPLATE_WATCH \
            $object_name

        python3 -m blue_geo.watch.targets save \
            --target_name $target_name \
            --object_name $object_name \
            "${@:4}"
        return
    fi

    if [[ "$task" == "publish" ]]; then
        abcli_publish \
            as=geo-watch-targets,suffix=.yaml \
            $BLUE_GEO_WATCH_TARGET_LIST
        return
    fi

    if [[ ",upload,test," == *",$task,"* ]]; then
        python3 -m blue_geo.watch.targets test
        [[ $? -ne 0 ]] && return 1
    fi

    if [[ "$task" == "upload" ]]; then
        blue_geo_watch_targets \
            save \
            target=all \
            $BLUE_GEO_WATCH_TARGET_LIST
        [[ $? -ne 0 ]] && return 1

        abcli_$task - $BLUE_GEO_WATCH_TARGET_LIST
        return
    fi

    if [[ "$task" == "test" ]]; then
        return
    fi

    abcli_log_error "@targets: $task: command not found."
    return 1
}

abcli_source_path - caller,suffix=/targets
