import os

if not QGIS_is_live:
    from log import log_error

    ABCLI_OBJECT_ROOT = ""


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
