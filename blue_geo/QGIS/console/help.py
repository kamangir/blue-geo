if not QGIS_is_live:
    from .layer import Q_layer
    from .logger import Q_clear
    from .QGIS import QGIS
    from .project import Q_project


def Q_help(clear=False):
    if clear:
        Q_clear(log=False)

    for thing in [
        Q_layer,
        Q_project,
    ] + [app for app in QGIS.app_list if app.name != "template"]:
        thing.help()

    QGIS.help_()
