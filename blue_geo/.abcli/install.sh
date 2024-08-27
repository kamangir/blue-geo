#! /usr/bin/env bash

function abcli_install_blue_geo() {
    if [[ "$abcli_is_mac" == true ]]; then
        brew install gdal
    elif [[ "$abcli_is_ubuntu" == true ]] &&
        [[ "$abcli_is_github_workflow" == false ]]; then
        apt-get install -y gdal-bin
    fi
}

abcli_install_module blue_geo 1.2.1
