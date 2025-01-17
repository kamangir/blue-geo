if not QGIS_is_live:
    from ..help import Q_help


def test_help(deep: bool = False):
    Q_help()
