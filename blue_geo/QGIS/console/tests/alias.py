if not QGIS_is_live:
    from ..alias import upload


def test_aliases():
    upload(dryrun=True)
