#! /usr/bin/env bash

function blue_geo_watch_map() {
    local options=$1

    if [ $(abcli_option_int "$options" help 0) == 1 ]; then
        abcli_show_usage_2 blue_geo watch map
        return
    fi

    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not do_dryrun))
    local offset=$(abcli_option "$options" offset 0)
    local modality=$(abcli_option "$options" modality rgb)
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
        abcli_log_error "@geo: watch: map: offset=$offset: datacube-id not found."
        return 1
    fi

    abcli_log "🌐 @geo watch map $query_object_name @ $offset==$datacube_id -> /$suffix"

    blue_geo_datacube_ingest \
        dryrun=$do_dryrun,scope=rgbx \
        $datacube_id

    local object_name=$query_object_name-$suffix-$offset

    blue_geo_watch_targets copy - \
        $query_object_name \
        $object_name

    local crop_suffix=$(abcli_string_timestamp_short)
    blue_geo_datacube_crop \
        dryrun=$do_dryrun,suffix=$crop_suffix \
        $object_name \
        $datacube_id
    [[ $? -ne 0 ]] && return 1

    local cropped_datacube_id=$datacube_id-DERIVED-crop-$crop_suffix

    blue_geo_datacube_generate \
        dryrun=$do_dryrun \
        $cropped_datacube_id \
        --modality $modality
    [[ $? -ne 0 ]] && return 1

    local filename=$(blue_geo_datacube_list $cropped_datacube_id \
        --scope rgb \
        --log 0 \
        --count 1 \
        --exists 1)
    if [[ -z "$filename" ]]; then
        abcli_warn "@geo: watch: map: offset=$offset: $cropped_datacube_id: file not found."

        [[ "$do_upload" == 1 ]] &&
            abcli_upload - $object_name

        return 0
    fi
    cp -v \
        $ABCLI_OBJECT_ROOT/$cropped_datacube_id/$filename \
        $ABCLI_OBJECT_ROOT/$object_name/

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_geo.watch.workflow \
        map \
        --datacube_id "$datacube_id" \
        --object_name "$object_name" \
        --modality $modality \
        --offset $offset \
        "${@:4}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return $status
}
