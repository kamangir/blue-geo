#! /usr/bin/env bash

function test_blue_geo_watch_targets_get_catalog() {
    abcli_download - $BLUE_GEO_WATCH_TARGET_LIST

    abcli_assert \
        $(blue_geo_watch_targets get \
            --what catalog \
            --target_name Leonardo \
            --log 0) \
        SkyFox
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        "$(blue_geo_watch_targets get \
            --what catalog \
            --target_name Deadpool \
            --log 0)" \
        - empty
}

function test_blue_geo_watch_targets_get_collection() {
    abcli_download - $BLUE_GEO_WATCH_TARGET_LIST

    abcli_assert \
        $(blue_geo_watch_targets get \
            --what collection \
            --target_name Leonardo \
            --log 0) \
        Venus
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        "$(blue_geo_watch_targets get \
            --what collection \
            --target_name Deadpool \
            --log 0)" \
        - empty
}

function test_blue_geo_watch_targets_get_exists() {
    abcli_download - $BLUE_GEO_WATCH_TARGET_LIST

    abcli_assert \
        $(blue_geo_watch_targets get \
            --what exists \
            --target_name Leonardo \
            --log 0) \
        1
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        $(blue_geo_watch_targets get \
            --what exists \
            --target_name Deadpool \
            --log 0) \
        0
}

function test_blue_geo_watch_targets_get_query_args() {
    abcli_download - $BLUE_GEO_WATCH_TARGET_LIST

    abcli_assert \
        $(blue_geo_watch_targets get \
            --what query_args \
            --target_name Leonardo \
            --log 0 \
            --delim +) \
        Venus
    [[ $? -ne 0 ]] && return 1

    abcli_assert \
        "$(blue_geo_watch_targets get \
            --what query_args \
            --target_name Deadpool \
            --log 0 \
            --delim +)" \
        - empty
}
