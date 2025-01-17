from typing import List

if not QGIS_is_live:
    from ..layer import layer
    from ..project import project


def Q_test_assets_object_references(
    deep: bool = False,
) -> List[str]:
    output = [
        project,
        "project",
        "qgz",
        #
        layer,
        "layer",
        #
        "object",
        object,
    ]

    if not deep:
        output = [output[0]]

    return output
