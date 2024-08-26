#! /usr/bin/env bash

function blue_geo_watch_map() {
    local what=$1

    if [[ "$what" == help ]]; then
        local options="$(xtra dryrun,~download,)offset=<offset>,suffix=<suffix>$(xtra ,~upload)"

        abcli_show_usage "@geo watch map $(xwrap $options '.|<query-object-name>')" \
            "@geo watch map <query-object-name> @ <offset> -> /<suffix>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not do_dryrun))
    local offset=$(abcli_option_int "$options" offset 0)
    local suffix=$(abcli_option "$options" suffix $(abcli_string_timestamp_short))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not do_dryrun))

    local query_object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $query_object_name

    local datacube_id=$(blue_geo_catalog_query_read - \
        $query_object_name \
        --count 1 \
        --offset $offset)
    if [[ -z "$datacube_id" ]]; then
        abcli_log_error "-@geo: watch: map: offset=$offset: datacube-id not found."
        return 1
    fi

    blue_geo_datacube_ingest \
        dryrun=$do_dryrun,what=quick \
        $datacube_id

    local object_name=$query_object_name-$suffix-$offset

    local target_path=$abcli_object_root/$object_name/target/
    mkdir -pv $target_path
    cp -v \
        $abcli_object_root/$query_object_name/target/* \
        $target_path

    abcli_log "🌐 @geo watch map $query_object_name @ $offset==$datacube_id -> /$suffix"

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.watch.workflow \
        map \
        --datacube_id "$datacube_id" \
        --object_name "$object_name" \
        "${@:4}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return $status
}
