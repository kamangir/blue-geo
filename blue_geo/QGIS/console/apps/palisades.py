import glob

if not QGIS_is_live:
    from ..logger import Q_log
    from ..application import BLUE_GEO_QGIS_APPLICATION
    from ..QGIS import QGIS
    from ..objects import Q_file_path_in_object, Q_file_name
    from ..project import Q_project
    from ..logger import Q_log_error, Q_verbose


class BLUE_GEO_QGIS_APPLICATION_PALISADES(BLUE_GEO_QGIS_APPLICATION):
    def __init__(self):
        super().__init__("palisades", "🧑🏽‍🚒")

    def help_(self):
        Q_log(
            "palisades.load",
            "load the layers of the palisades object.",
            icon=self.icon,
        )

    @property
    def load(self):
        metadata = Q_project.metadata
        if Q_verbose:
            self.log(f"metadata: {metadata}")

        if "predict" not in metadata:
            Q_log_error("predict not found in metadata.")
            return

        reference_filename = metadata["predict"]["reference_filename"]
        datacube_id = metadata["predict"]["datacube_id"]
        if not Q_project.add_layer(
            filename=Q_file_path_in_object(
                filename=reference_filename,
                object_name=datacube_id,
            ),
            layer_name=f"input-{reference_filename}",
        ):
            return

        output_filename = metadata["predict"]["output_filename"]
        if not Q_project.add_layer(
            filename=Q_file_path_in_object(
                filename=output_filename,
                object_name=Q_project.name,
            ),
            layer_name=f"predict-{output_filename}",
            template_name="prediction-template",
        ):
            return

        building_footprint_filename_list = glob.glob(
            Q_file_path_in_object(
                filename="*.gpkg",
                object_name=Q_project.name,
            )
        )
        if building_footprint_filename_list:
            filename = building_footprint_filename_list[0]
            if not Q_project.add_layer(
                filename=filename,
                layer_name=Q_file_name(filename),
                template_name=f"{Q_file_name(filename)}-template",
            ):
                return


palisades = BLUE_GEO_QGIS_APPLICATION_PALISADES()
QGIS.add_app(palisades)
