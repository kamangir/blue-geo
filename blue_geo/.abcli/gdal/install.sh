#! /usr/bin/env bash

function blue_geo_gdal_install() {
    if [[ "$abcli_is_mac" == true ]]; then
        brew install gdal
        return
    fi

    if [[ "$abcli_is_ubuntu" == true ]] &&
        [[ "$abcli_is_github_workflow" == false ]] &&
        [[ "$abcli_is_docker" == false ]]; then
        # sudo add-apt-repository ppa:ubuntugis/ppa
        sudo apt-get update
        sudo apt-get install -y gdal-bin python3-gdal
    fi
}
