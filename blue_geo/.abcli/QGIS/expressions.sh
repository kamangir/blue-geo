#! /usr/bin/env bash

function blue_geo_QGIS_expressions() {
    local task=$1

    if [ "$task" == help ]; then
        abcli_show_usage "QGIS expressions pull" \
            "pull QGIS expressions."
        abcli_show_usage "QGIS expressions push [push]" \
            "push QGIS expressions."

        abcli_log " 📂 $abcli_QGIS_path_expressions"
        abcli_log " 📂 $abcli_QGIS_path_expressions_git"
        return
    fi

    if [[ "$task" == pull ]]; then
        rsync -av \
            "$abcli_QGIS_path_expressions_git/" \
            "$abcli_QGIS_path_expressions/"
        return
    fi

    if [[ "$task" == push ]]; then
        local options=$2
        local do_push=$(abcli_option_int "$options" push 0)

        rsync -av \
            --exclude='__pycache__' \
            --exclude='default.py' \
            --exclude='__init__.py' \
            "$abcli_QGIS_path_expressions/" \
            "$abcli_QGIS_path_expressions_git/"

        if [[ "$do_push" == 1 ]]; then
            abcli_git blue-geo push \
                "$(python3 -m blue_geo version) QGIS expressions"
        else
            abcli_git blue-geo status ~all
        fi

        return
    fi

    abcli_log_error "-QGIS: expressions: $task: command not found."
    return 1
}
