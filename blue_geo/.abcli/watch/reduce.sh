#! /usr/bin/env bash

function blue_geo_watch_reduce() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        local options="$(xtra dryrun,~download,)suffix=<suffix>$(xtra ~upload)"

        abcli_show_usage "@geo watch reduce $(xwrap $options '..|<query-object-name>' '.|<object-name>')" \
            "@geo watch reduce <query-object-name>/<suffix> -> <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not do_dryrun))
    local suffix=$(abcli_option "$options" suffix)
    if [[ -z "$suffix" ]]; then
        abcli_log_error "-@geo: watch: reduce: suffix not found."
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
            cp,~meta \
            $leaf_object_name \
            $object_name

        offset=$((offset + 1))
    done

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.watch.workflow \
        reduce \
        --query_object_name $query_object_name \
        --suffix $suffix \
        --object_name $object_name \
        "${@:4}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return $status
}
