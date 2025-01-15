#! /usr/bin/env bash

function test_blue_geo_logging() {
    local options=$1

    blue_geo log \
        filename=1050010040277300-visual.tif,$options \
        datacube-Maxar-Open-Data-WildFires-LosAngeles-Jan-2025-11-031311103030-1050010040277300
}
