if not QGIS_is_live:
    from log import log


class BLUE_GEO_QGIS_APPLICATION(object):
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon

        log(self.name, "", icon=self.icon)

    def log(self, message, note=""):
        log(message, note, icon=self.icon)
