#! /usr/bin/env bash

export BLUE_GEO_QGIS_PATH_PROFILE="$HOME/Library/Application Support/QGIS/QGIS3/profiles/default"
export BLUE_GEO_QGIS_PATH_EXPRESSIONS=$BLUE_GEO_QGIS_PATH_PROFILE/python/expressions
export BLUE_GEO_QGIS_PATH_EXPRESSIONS_GIT=$abcli_path_git/blue-geo/blue_geo/QGIS/expressions
export BLUE_GEO_QGIS_PATH_SHARED=$HOME/Downloads/QGIS
export BLUE_GEO_QGIS_PATH_SERVER=$BLUE_GEO_QGIS_PATH_SHARED/server
export BLUE_GEO_QGIS_PATH_TEMPLATES=$BLUE_GEO_QGIS_PATH_PROFILE/project_templates

export BLUE_GEO_QGIS_TEMPLATES_OBJECT_NAME=QGIS-templates-v1

mkdir -p $BLUE_GEO_QGIS_PATH_SERVER

# internal function to abcli_seed.
function abcli_seed_QGIS() {
    # seed is NOT local
    seed=$(python3 -m blue_geo.QGIS generate_seed)
}

function blue_geo_QGIS() {
    local task=$(abcli_unpack_keyword $1 help)

    local function_name=blue_geo_QGIS_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    if [ "$task" == "seed" ]; then
        abcli_seed QGIS "${@:2}"
        return
    fi

    abcli_log_error "-QGIS: $task: command not found."
    return 1
}

abcli_source_caller_suffix_path /QGIS
