import os

if not QGIS_is_live:
    from .graphics import Q_refresh
    from .logger import Q_log_error, Q_log
    from .project import Q_project

    from .mock import iface

    ABCLI_OBJECT_ROOT = ""


class ABCLI_QGIS_Layer(object):
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
