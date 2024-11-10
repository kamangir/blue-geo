function blue_geo_QGIS_download() {
    local object_name=$(abcli_clarify_object $1 .)

    abcli_download filename=$object_name.qgz $object_name
    [[ $? -ne 0 ]] && return 1

    local object_path=$ABCLI_OBJECT_ROOT/$object_name
    local qgz_filename=$object_path/$object_name.qgz

    local list_of_dependencies=$(python3 -m blue_geo.QGIS \
        list_dependencies \
        --filename "$qgz_filename" \
        --delim +)
    abcli_log_list "$list_of_dependencies" \
        --before "downloading" \
        --after "dependenci(es)" \
        --delim +

    local dependency_name
    for dependency_name in $(echo $list_of_dependencies | tr + " "); do
        [[ "$dependency_name" == "$object_name" ]] && continue
        abcli_download - $dependency_name
    done

    abcli_download - $object_name \
        QGIS,"${@:2}"
}
