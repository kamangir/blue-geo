#! /usr/bin/env bash

function ukraine_timemap_browse() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="dataset|github"
        abcli_show_usage "ukraine_timemap browse$ABCUL[$options]" \
            "browse ukraine-timemap."
        return
    fi

    local do_dataset=$(abcli_option_int "$options" dataset 0)
    local do_github=$(abcli_option_int "$options" github 0)

    local url="https://ukraine.bellingcat.com/"
    [[ "$do_github" == 1 ]] &&
        url="https://github.com/bellingcat/ukraine-timemap"
    [[ "$do_dataset" == 1 ]] &&
        url="https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json"

    abcli_browse $url
}
