if not QGIS_is_live:
    from ..application import BLUE_GEO_QGIS_APPLICATION
    from ..file import Q_file_exists
    from ..logger import Q_log, Q_log_error
    from ..objects import Q_file_path_in_object
    from ..project import Q_project
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
        datacube_id = Q_project.name

        filename = Q_file_path_in_object(
            filename="label.shp",
            object_name=datacube_id,
        )

        if not Q_file_exists(filename):
            Q_log_error(f"file not found: {filename}")
            Q_log(f'try running "@datacube label - {datacube_id}".')
            return

        Q_project.add_layer(
            filename=filename,
            layer_name=f"label-{datacube_id}",
            template_name="template-label",
        )


datacube = BLUE_GEO_QGIS_APPLICATION_DATACUBE()
QGIS.add_app(datacube)
