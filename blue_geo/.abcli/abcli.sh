#! /usr/bin/env bash

abcli_source_path - caller,suffix=/tests

abcli_env dot load \
    plugin=blue_geo
abcli_env dot load \
    filename=blue_geo/config.env,plugin=blue_geo


