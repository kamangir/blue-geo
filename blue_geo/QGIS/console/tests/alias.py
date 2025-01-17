if not QGIS_is_live:
    from ..alias import Q, clear, upload
    from ..QGIS import ABCLI_QGIS


def test_aliases(deep: bool = False):
    assert isinstance(Q, ABCLI_QGIS)

    clear()

    upload(dryrun=True)
