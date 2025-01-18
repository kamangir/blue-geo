if not QGIS_is_live:
    from ..logger import Q_log
    from ..application import BLUE_GEO_QGIS_APPLICATION
    from ..QGIS import QGIS


class BLUE_GEO_QGIS_APPLICATION_DATACUBE(BLUE_GEO_QGIS_APPLICATION):
    def __init__(self):
        super().__init__("datacube", "🧊")

    def help_(self):
        Q_log(
            "datacube.label",
            "label the datacube.",
            icon=self.icon,
        )

    @property
    def label(self):
        self.log("🪄")


datacube = BLUE_GEO_QGIS_APPLICATION_DATACUBE()
QGIS.add_app(datacube)
