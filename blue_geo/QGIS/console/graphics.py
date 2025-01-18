if not QGIS_is_live:
    from .logger import Q_log
    from .objects import Q_file_path_in_object
    from .project import Q_project
    from .string import Q_timestamp

    from .mock import iface, qgis


def Q_refresh(deep=False):
    Q_log("{}refresh.".format("deep" if deep else ""))

    if deep:
        # https://api.qgis.org/api/classQgsMapCanvas.html
        iface.mapCanvas().redrawAllLayers()
    else:
        iface.mapCanvas().refresh()


def Q_screenshot(filename=""):
    filename = Q_file_path_in_object(
        filename=filename if filename else f"{Q_timestamp()}.png",
        object_name=Q_project.name,
    )

    qgis.utils.iface.mapCanvas().saveAsImage(filename)

    Q_log(filename, icon="🖼️")
