#! /usr/bin/env bash

function blue_geo_watch_reduce() {
    local what=$1

    if [[ "$what" == help ]]; then
        local options="$(xtra dryrun,~download,~upload)"

        abcli_show_usage "@geo watch reduce $(xwrap $options '.|<object-name>')" \
            "@geo watch reduce <object-name>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not do_dryrun))
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not do_dryrun))

    local object_name=$(abcli_clarify_object $2 .)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.watch.workflow \
        reduce \
        --object_name "$object_name" \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return $status
}
