if not QGIS_is_live:
    from logger import Q_hr, Q_log, Q_log_error, Q_verbose
    from ..layer import layer


def test_layer_properties(
    deep: bool = False,
): ...
