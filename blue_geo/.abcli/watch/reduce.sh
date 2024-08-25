#! /usr/bin/env bash

function blue_geo_watch_reduce() {
    local what=$1

    if [[ "$what" == help ]]; then
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

    local object_path=$abcli_object_root/$object_name
    mkdir -pv $object_path
    cp -v \
        $abcli_object_root/$query_object_name/target.* \
        $object_path

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
