from typing import List

if not QGIS_is_live:
    from logger import Q_log


class BLUE_GEO_QGIS_APPLICATION:
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon

        self.log(self.name)

    def help(self):
        pass

    def log(self, message, note=""):
        Q_log(message, note, icon=self.icon)
