if not QGIS_is_live:
    from .logger import Q_clear
    from .QGIS import QGIS


def Q_help(clear=False):
    if clear:
        Q_clear(log=False)

    for thing in [app for app in QGIS.app_list if app.name != "template"] + [QGIS]:
        thing.help_()
