if not QGIS_is_live:
    from .string import Q_timestamp


def test_timestamp(deep: bool = False):
    assert Q_timestamp()
