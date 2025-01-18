if not QGIS_is_live:
    from .string import Q_timestamp


def test_timestamp():
    assert Q_timestamp()
