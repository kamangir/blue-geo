if not QGIS_is_live:
    from QGIS import QGIS

Q = QGIS


def clear():
    QGIS.clear()


def upload(what=""):
    QGIS.upload(what)
