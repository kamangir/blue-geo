#! /usr/bin/env bash

function blue_geo_datacube_list() {
    local datacube_id=$(abcli_clarify_object $1 .)

    if [[ "$datacube_id" == "help" ]]; then
        local scope_help=$(python3 -c "from blue_geo.catalog.generic.generic.scope import DatacubeScope; print(DatacubeScope.help)")
        local args="[--count 1]$ABCUL[--delim +]$ABCUL[--exists 1]$ABCUL[--log 0]$ABCUL[--scope $scope_help]"
        abcli_show_usage "@datacube list$ABCUL[.|<datacube-id>]$ABCUL$args" \
            "list datacube files."
        return
    fi

    python3 -m blue_geo.datacube \
        list \
        --datacube_id $datacube_id \
        "${@:2}"
}
