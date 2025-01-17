import os

if not QGIS_is_live:
    from .graphics import Q_refresh
    from .logger import Q_log_error, Q_log
    from .project import Q_project

    from .mock import (
        QgsRasterLayer,
        QgsProject,
        QgsMapLayerStyle,
        QgsVectorLayer,
        iface,
    )

    ABCLI_OBJECT_ROOT = ""


class ABCLI_QGIS_Layer(object):
    def add_layer(
        self,
        filename: str,
        layer_name: str,
        template_name: str = "",
        set_nodata: bool = False,
        nodata: int = 0,
        refresh: bool = True,
        verbose: bool = True,
    ):
        if self.exists(layer_name, verbose=verbose):
            return True

        if filename.endswith(".geojson"):
            layer_ = QgsVectorLayer(filename, layer_name, "ogr")
        elif filename.endswith(".tif"):
            layer_ = QgsRasterLayer(filename, layer_name)
        else:
            Q_log_error(f"cannot load {filename}.")
            return False

        if not layer_.isValid():
            Q_log_error(f"invalid layer: {filename}.")
            return False

        QgsProject.instance().addMapLayer(layer_)

        if layer_ and layer_.dataProvider() and set_nodata:
            layer_.dataProvider().setNoDataValue(1, nodata)
            layer_.dataProvider().reloadData()
            layer_.triggerRepaint()

        if template_name:
            template_layer = Q_project.get_layer(template_name)
            if not len(template_layer):
                Q_log_error(f"template not found: {template_name}.")
                return False

            # https://gis.stackexchange.com/a/357206/210095
            source_style = QgsMapLayerStyle()
            source_style.readFromLayer(template_layer[0])
            source_style.writeToLayer(layer_)
            layer_.triggerRepaint()

        Q_log(
            layer_name,
            template_name,
            icon="🎨",
        )

        if refresh:
            Q_refresh()

    def help(self):
        pass

    @property
    def filename(self):
        try:
            return iface.activeLayer().dataProvider().dataSourceUri()
        except:
            Q_log_error("layer.filename not found.")
            return ""

    @property
    def name(self):
        filename = self.filename
        return filename.split(os.sep)[-1].split(".")[0] if filename else ""

    @property
    def object_name(self):
        filename = self.filename
        if not filename:
            return ""

        if ABCLI_OBJECT_ROOT not in filename:
            return ""

        tokens = filename.split(f"{ABCLI_OBJECT_ROOT}/", 1)[1].split("/")
        if not tokens:
            return ""

        return tokens[0]

    @property
    def path(self):
        return os.path.dirname(self.filename)


Q_layer = ABCLI_QGIS_Layer()
