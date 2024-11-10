#! /usr/bin/env bash

function blue_geo_QGIS_expressions() {
    local task=$1

    if [[ "$task" == pull ]]; then
        rsync \
            -avv --progress \
            "$BLUE_GEO_QGIS_PATH_EXPRESSIONS_GIT/" \
            "$BLUE_GEO_QGIS_PATH_EXPRESSIONS/"
        return
    fi

    if [[ "$task" == push ]]; then
        local options=$2
        local do_push=$(abcli_option_int "$options" push 0)

        rsync \
            -avv --progress \
            --exclude='__pycache__' \
            --exclude='default.py' \
            --exclude='__init__.py' \
            "$BLUE_GEO_QGIS_PATH_EXPRESSIONS/" \
            "$BLUE_GEO_QGIS_PATH_EXPRESSIONS_GIT/"

        return
    fi

    abcli_log_error "QGIS: expressions: $task: command not found."
    return 1
}
