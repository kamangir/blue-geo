#! /usr/bin/env bash

function blue_geo_watch_reduce() {
    local options=$1
    local algo=$(abcli_option "$options" algo modality)
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not do_dryrun))
    local do_publish=$(abcli_option_int "$options" publish 0)
    local suffix=$(abcli_option "$options" suffix)
    if [[ -z "$suffix" ]]; then
        abcli_log_error "@geo: watch: reduce: suffix not found."
        return 1
    fi

    local query_object_name=$(abcli_clarify_object $2 ..)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $query_object_name

    local object_name=$(abcli_clarify_object $3 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    blue_geo_watch_targets copy - \
        $query_object_name \
        $object_name

    abcli_log "🌐 @geo watch reduce $query_object_name/$suffix -> $object_name"

    local datacube_id_list=$(abcli_metadata get \
        delim=space,key=datacube_id,object \
        $query_object_name)
    abcli_log_list "$datacube_id_list" \
        --before "reducing" \
        --delim space \
        --after "datacube(s)"

    local datacube_id
    local offset=0
    local leaf_object_name
    for datacube_id in $datacube_id_list; do
        leaf_object_name=$query_object_name-$suffix-$(python3 -c "print(f'{$offset:03d}')")
        abcli_log "reducing $leaf_object_name ..."

        abcli_clone \
            cp,~relate,~tags \
            $leaf_object_name \
            $object_name

        offset=$((offset + 1))
    done

    abcli_eval - \
        blue_geo_watch_algo_${algo}_reduce "$@"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    if [[ "$do_publish" == 1 ]]; then
        abcli_publish tar $object_name
        abcli_publish suffix=.gif $object_name
    fi

    return $status
}
