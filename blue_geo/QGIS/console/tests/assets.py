from typing import List

if not QGIS_is_live:
    from ..layer import Q_layer
    from ..project import Q_project


Q_test_assets_object_references = [
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
