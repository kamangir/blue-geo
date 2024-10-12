#! /usr/bin/env bash

abcli_source_caller_suffix_path /tests

abcli_env_dot_load \
    caller,ssm,plugin=blue_geo,suffix=/../..

abcli_env_dot_load \
    caller,filename=config.env,suffix=/..
