#! /usr/bin/env bash

function blue_geo_datacube_crop() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not do_dryrun))
    local suffix=$(abcli_option "$options" suffix $(abcli_string_timestamp_short))

    local object_name=$(abcli_clarify_object $2 ..)
    [[ "$do_download" == 1 ]] &&
        abcli_download - $object_name

    local cutline=$ABCLI_OBJECT_ROOT/$object_name/target/shape.geojson
    if [[ ! -f "$cutline" ]]; then
        abcli_log_error "@datacube: crop: $cutline: file not found."
        return 1
    fi

    local datacube_id=$(abcli_clarify_object $3 .)

    local cropped_datacube_id=$datacube_id-DERIVED-crop-$suffix

    blue_geo_watch_targets copy - \
        $object_name \
        $cropped_datacube_id

    local list_of_files=$(blue_geo_datacube_list $datacube_id \
        --delim space \
        --exists 1 \
        --scope raster \
        --log 0)
    local filename
    local source_filename
    local destination_filename
    for filename in $list_of_files; do
        source_filename=$ABCLI_OBJECT_ROOT/$datacube_id/$filename

        abcli_log "cropping $filename ..."

        destination_filename=$ABCLI_OBJECT_ROOT/$cropped_datacube_id/$filename
        destination_path=$(dirname "$destination_filename")
        mkdir -pv $destination_path

        abcli_eval dryrun=$do_dryrun \
            gdalwarp -cutline $cutline \
            -crop_to_cutline \
            -dstalpha \
            $source_filename \
            $destination_filename
        # [[ $? -ne 0 ]] && return 1
    done

    return 0
}
