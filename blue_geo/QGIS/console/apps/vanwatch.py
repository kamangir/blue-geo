import os
import glob

if not QGIS_is_live:
    from application import BLUE_GEO_QGIS_APPLICATION
    from log import log
    from project import project
    from QGIS import QGIS


class BLUE_GEO_QGIS_APPLICATION_VANWATCH(BLUE_GEO_QGIS_APPLICATION):
    def __init__(self):
        super().__init__("vanwatch", "🌈")

    def help(self):
        self.log(
            "vanwatch.list_layers()",
            "list vanwatch layers.",
        )
        self.log(
            "vanwatch.load(count=<count>, timed=True, offset=<offset>, prefix=<prefix>)",
            "load layers.",
        )
        self.log(
            "vanwatch.unload(prefix)",
            "unload prefix*.",
        )

    def list_layers(self):
        return sorted(
            [
                os.path.splitext(os.path.basename(filename))[0]
                for filename in glob.glob(
                    os.path.join(
                        project.path,
                        "*.geojson",
                    )
                )
            ]
        )

    def load(
        self,
        prefix="",
        count=-1,
        offset=0,
        refresh=True,
        timed=False,
    ) -> bool:
        list_layers = self.list_layers()

        list_layers = list(reversed(list_layers))
        if offset:
            list_layers = list_layers[offset:]
        if count != -1:
            list_layers = list_layers[:count]

        for layer_name in list_layers:
            if not layer_name.startswith(prefix):
                continue

            filename = os.path.join(project.path, f"{layer_name}.geojson")

            QGIS.load(
                filename,
                layer_name,
                "template-timed" if timed else "template",
                refresh=False,
            )

        self.log(f"loaded {len(list_layers)} layer(s).")

        if refresh:
            QGIS.refresh()

    def unload(self, prefix="", refresh=True):
        log(prefix, icon="🗑️")

        for layer_name in [
            layer_name
            for layer_name in QGIS.list_of_layers()
            if layer_name.startswith(prefix)
        ]:
            QGIS.unload(layer_name, refresh=False)

        if refresh:
            QGIS.refresh()


vanwatch = BLUE_GEO_QGIS_APPLICATION_VANWATCH()
QGIS.add_application(vanwatch)
