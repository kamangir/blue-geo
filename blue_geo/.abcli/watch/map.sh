#! /usr/bin/env bash

function blue_geo_watch_map() {
    local what=$1

    if [[ "$what" == help ]]; then
        local options="$(xtra dryrun,~download,~upload)"

        abcli_show_usage "@geo watch map $(xwrap $options '.|<datacube-id>' '-|<object-name>')" \
            "@geo watch map <datacube-id> -> <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not do_dryrun))

    local datacube_id=$(abcli_clarify_object $2 .)
    blue_geo_datacube_ingest \
        dryrun=$do_dryrun,what=quick \
        $datacube_id

    local object_name=$(abcli_clarify_object $3 $(abcli_string_timestamp))
    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

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
