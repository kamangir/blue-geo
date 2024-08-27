#! /usr/bin/env bash

function blue_geo_datacube_crop() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        options="download,dryrun,suffix=<suffix>"
        abcli_show_usage "@datacube crop$ABCUL[$options]$ABCUL[..|<object-name>]$ABCUL[.|<datacube-id>]$ABCUL" \
            "crop <datacube-id> by <object-name>/target/shape.geojson -> <datacube-id>-DERIVED-crop-<suffix>."
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not do_dryrun))
    local suffix=$(abcli_option "$options" suffix $(abcli_string_timestamp_short))

    local object_name=$(abcli_clarify_object $2 ..)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    local datacube_id=$(abcli_clarify_object $3 .)

    local cropped_datacube_id=$datacube_id-DERIVED-crop-$suffix

    blue_geo_watch_targets copy - \
        $object_name \
        $cropped_datacube_id

    local list_of_files=$(blue_geo_datacube_get list_of_files \
        $datacube_id \
        --suffix .jp2+.tif+.tiff)
    abcli_log_list "$list_of_files" \
        --before "cropping" \
        --delim + \
        --after "file(s)"

    echo "🪄"

    return 0
}
