if not QGIS_is_live:
    from .alias import Q_alias_help
    from .graphics import Q_graphics_help
    from .layer import Q_layer
    from .logger import Q_clear
    from .objects import Q_objects_help
    from .QGIS import QGIS, Q_QGIS_help
    from .project import Q_project
    from .testing import Q_testing_help


def Q_help(clear=False):
    if clear:
        Q_clear()

    for thing in [
        Q_layer,
        Q_project,
    ] + [app for app in QGIS.app_list if app.name != "template"]:
        thing.help()

    for func in [
        Q_graphics_help,
        Q_testing_help,
        Q_objects_help,
        Q_QGIS_help,
        Q_alias_help,
    ]:
        func()
