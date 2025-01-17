from typing import List

if not QGIS_is_live:
    from .assets import Q_test_assets_object_references
    from ..logger import Q_hr, Q_log, Q_log_error, Q_verbose
    from ..QGIS import QGIS
