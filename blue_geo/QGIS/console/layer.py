import os

if not QGIS_is_live:
    from log import log_error

    ABCLI_OBJECT_ROOT = ""


class ABCLI_QGIS_Layer(object):
    def add_raster(
        self,
        filename: str,
        layer_name: str = "",
        template_name: str = "",
        set_nodata: bool = False,
        nodata: int = 0,
        verbose: bool = True,
    ) -> bool:
        layer_name = layer.get_layer_name(filename, layer_name)

        if self.exists(layer_name, verbose):
            return True

        layer_ = QgsRasterLayer(filename, layer_name)
        if not layer_.isValid():
            log_error(f"invalid filename: {filename}")
            return False

        QgsProject.instance().addMapLayer(layer_)

        if layer_ and layer_.dataProvider() and set_nodata:
            layer_.dataProvider().setNoDataValue(1, nodata)
            layer_.dataProvider().reloadData()
            layer_.triggerRepaint()

        if template_name:
            template_layer = QgsProject.instance().mapLayersByName(template_name)
            if not len(template_layer):
                log_error(f"template {template_name} not found for layer {layer_name}.")
                return False

            # https://gis.stackexchange.com/a/357206/210095
            source_style = QgsMapLayerStyle()
            source_style.readFromLayer(template_layer[0])
            source_style.writeToLayer(layer_)
            layer_.triggerRepaint()

        log(
            layer_name,
            template_name if verbose else "",
            icon="🎨",
        )

        return True

    def add_vector(
        self,
        filename: str,
        layer_name: str = "",
        template_name: str = "",
        verbose: bool = True,
    ) -> bool:
        layer_name = layer.get_layer_name(filename, layer_name)

        if self.exists(layer_name, verbose):
            return True

        layer_ = QgsVectorLayer(filename, layer_name, "ogr")
        if not layer_.isValid():
            log_error(f"invalid layer: {filename}")
            return False

        QgsProject.instance().addMapLayer(layer_)

        if template_name:
            template_layer = QgsProject.instance().mapLayersByName(template_name)
            if not len(template_layer):
                log_error(f"{template_name} not found for {layer_name}.")
                return False

            # https://gis.stackexchange.com/a/357206/210095
            source_style = QgsMapLayerStyle()
            source_style.readFromLayer(template_layer[0])
            source_style.writeToLayer(layer_)
            layer_.triggerRepaint()

        log(
            layer_name,
            template_name if verbose else "",
            icon="🎨",
        )

    def exists(
        self,
        layer_name: str,
        verbose: bool = True,
    ) -> bool:
        layer_ = QgsProject.instance().mapLayersByName(layer_name)

        if len(layer_) > 0:
            if verbose:
                log(layer_name, icon="✅")
            return True

        return False

    def help(self):
        pass

    @property
    def filename(self):
        try:
            return iface.activeLayer().dataProvider().dataSourceUri()
        except:
            log_error("unknown layer.filename.")
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


layer = ABCLI_QGIS_Layer()
