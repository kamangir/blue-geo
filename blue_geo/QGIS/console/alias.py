if not QGIS_is_live:
    from QGIS import QGIS


def clear():
    QGIS.clear()


def upload(object_name=""):
    QGIS.upload(object_name)
