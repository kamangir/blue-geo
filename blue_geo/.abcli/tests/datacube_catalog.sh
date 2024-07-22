#! /usr/bin/env bash

function test_blue_geo_datacube_catalog() {
    abcli_eval dryrun=$do_dryrun \
        blue_geo datacube list catalogs
}
