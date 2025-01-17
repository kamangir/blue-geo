from typing import List

if not QGIS_is_live:
    from ..layer import Q_layer
    from ..project import Q_project


def Q_test_assets_object_references(
    deep: bool = False,
) -> List[str]:
    output = [
        Q_project,
        "project",
        "qgz",
        #
        Q_layer,
        "layer",
        #
        "object",
        object,
    ]

    if not deep:
        output = [output[0]]

    return output
