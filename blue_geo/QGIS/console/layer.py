import os

if not QGIS_is_live:
    from log import log_error


class ABCLI_QGIS_Layer(object):
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
        return filename.split(os.sep)[-2] if filename else ""

    @property
    def path(self):
        return os.path.dirname(self.filename)


layer = ABCLI_QGIS_Layer()
