if not QGIS_is_live:
    from logger import log, log_error, verbose, hr
    from ..layer import layer


def test_layer_properties(
    deep: bool = False,
): ...
