#! /usr/bin/env bash

abcli_source_path - caller,suffix=/tests

abcli_env dot load \
    plugin=blue_plugin
abcli_env dot load \
    filename=blue_plugin/config.env,plugin=blue_plugin
