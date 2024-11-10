import os
import xml.etree.ElementTree as ET
import shutil
from typing import List


def list_of_dependencies(
    filename: str,
    ABCLI_OBJECT_ROOT: str,
    verbose: bool = False,
) -> List[str]:
    file_path = os.path.dirname(filename)

    if filename.endswith(".qgz"):
        temp_dir = os.path.join(file_path, "_QGIS_temp")
        os.makedirs(temp_dir, exist_ok=True)

        os.system(f'unzip -q -o "{filename}" -d "{temp_dir}"')

        found = False
        for filename_ in os.listdir(temp_dir):
            if filename_.endswith(".qgs"):
                filename = filename.replace(".qgz", ".qgs")
                shutil.copy(os.path.join(temp_dir, filename_), filename)
                found = True
        shutil.rmtree(temp_dir)
        if not found:
            return []

    # Load QGS file as XML
    tree = ET.parse(filename)
    root = tree.getroot()

    layer_elements = root.findall(".//maplayer")

    list_of_objects = []
    for layer_element in layer_elements:
        datasource = layer_element.find("datasource")
        if datasource is None or not datasource.text:
            continue

        layer_filename = os.path.abspath(
            os.path.join(file_path, os.path.dirname(datasource.text))
        )
        if verbose:
            print(f"skipped {layer_filename}")

        if ABCLI_OBJECT_ROOT not in layer_filename:
            if verbose:
                print(f"skipped {layer_filename}")
            continue

        tokens = layer_filename.split(f"{ABCLI_OBJECT_ROOT}/", 1)[1].split("/")
        if not tokens:
            if verbose:
                print(f"skipped {layer_filename}")
            continue

        object_name = tokens[0]
        if verbose:
            print(f"included {object_name}: {layer_filename}")
        list_of_objects += [object_name]

    return sorted(list(set(list_of_objects)))
