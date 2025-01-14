#! /usr/bin/env bash

function blue_geo_maxar_open_data_ingest() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_download=$(abcli_option_int "$options" download $(abcli_not $do_dryrun))
    local do_gdal=$(abcli_option_int "$options" gdal 1)
    local do_rm=$(abcli_option_int "$options" rm 1)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))
    local event_name=$(abcli_option "$options" event default)

    local object_name=$(abcli_clarify_object $2 $event_name-ingest-$(abcli_string_timestamp_short))

    abcli_log "ingesting $event_name -> $object_name ..."

    local object_path=$ABCLI_OBJECT_ROOT/$object_name
    mkdir -pv $object_path

    pushd $object_path >/dev/null

    # https://github.com/microsoft/building-damage-assessment/blob/main/SATELLITE_WORKFLOW.md#1-image-acquisition-and-label-generation
    mkdir -pv raw
    cd raw

    if [[ "$do_download" == 1 ]]; then
        # TODO: use $event_name and $count (options +=)

        abcli_eval ,$options \
            wget https://maxar-opendata.s3.amazonaws.com/events/Maui-Hawaii-fires-Aug-23/ard/04/122000330002/2023-08-12/10300100EB15FF00-visual.tif
        [[ $? -ne 0 ]] && return 1

        abcli_eval ,$options \
            wget https://maxar-opendata.s3.amazonaws.com/events/Maui-Hawaii-fires-Aug-23/ard/04/122000330020/2023-08-12/10300100EB15FF00-visual.tif
        [[ $? -ne 0 ]] && return 1
    fi

    if [[ "$do_gdal" == 1 ]]; then
        abcli_eval ,$options \
            gdalbuildvrt maxar_lahaina_8_12_2023-visual.vrt *.tif*
        [[ $? -ne 0 ]] && return 1

        abcli_eval ,$options \
            gdalwarp -co BIGTIFF=YES -co NUM_THREADS=ALL_CPUS -co COMPRESS=LZW -co PREDICTOR=2 -of COG maxar_lahaina_8_12_2023-visual.vrt maxar_lahaina_8_12_2023-visual.tif
        [[ $? -ne 0 ]] && return 1
    fi

    if [[ "$do_rm" == 1 ]]; then
        abcli_log "removing raw data ..."
        rm -v 10300100EB15FF00-visual.tif*
        rm -v maxar_lahaina_8_12_2023-visual.vrt
    fi

    popd >/dev/null

    abcli_eval dryrun=$do_dryrun \
        python3 -m blue_sandbox.microsoft_building_damage_assessment \
        ingest \
        --event_name $event_name \
        --object_name $object_name \
        "${@:3}"
    local status="$?"

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name

    return $status
}
