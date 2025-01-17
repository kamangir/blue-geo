if not QGIS_is_live:
    from .application import Q_app_list
    from .layer import Q_layer
    from .logger import Q_clear, Q_hr, Q_log, Q_log_error, Q_verbose
    from .project import Q_project
    from .QGIS import QGIS


def Q_help(clear=False):
    if clear:
        Q_clear()

    Q_log("clear()", "clear Python Console.")

    Q_layer.help()

    Q_log("Q_screenshot([filename],[object_name])", "screenshot.")

    Q_log("Q.load(filename,layer_name,template_name)", "load a layer.")

    Q_log('Q.open(" | <object-name> | layer | project")', "open.")

    Q_project.help()

    Q_log("Q_refresh()", "refresh.")
    Q_log("Q.reload()", "reload all layers.")

    Q_log("Q.unload(layer_name)", "unload layer_name.")

    Q_log('upload(" | <object-name> | layer | project | qgz")', "upload.")

    Q_log("Q_test(deep=True)", f"test Q.")

    Q_log("Q_verbose  = True|False", "set Q's verbose state.")

    Q_app_list.help()

    QGIS.help()
