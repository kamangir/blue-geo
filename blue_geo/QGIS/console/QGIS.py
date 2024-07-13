import os
import time
import random
from tqdm import tqdm


if not QGIS_is_live:
    from log import log, log_error, verbose
    from layer import layer
    from project import project
    from seed import seed

NAME = "blue_geo.QGIS"

VERSION = "5.14.1"

abcli_object_root = os.path.join(
    os.getenv("HOME", ""),
    "storage/abcli",
)


class ABCLI_QGIS(object):
    def __init__(self):
        self.app_list = []
        self.object_name = self.timestamp()

    def add_application(self, app):
        self.app_list += [app]

    def intro(self):
        log(
            "{}-{}: {}".format(
                NAME,
                VERSION,
                ", ".join(
                    [
                        "{} {}".format(
                            app.name,
                            app.icon,
                        )
                        for app in self.app_list
                    ]
                ),
            )
        )
        log(
            'Type in "{}.help()" for help.'.format(
                "|".join(["Q"] + [app.name for app in self.app_list])
            )
        )

    def clear(self):
        # https://gis.stackexchange.com/a/480025/250728
        from qgis.PyQt.QtWidgets import QDockWidget

        consoleWidget = iface.mainWindow().findChild(QDockWidget, "PythonConsole")
        consoleWidget.widget().console.clearButton.trigger()

        self.intro()

    def create_video(self, filename="QGIS", object_name=""):
        seed(
            [
                "abcli",
                "create_video",
                f"png,fps=2,filename={filename},gif",
                object_name if object_name else self.object_name,
            ]
        )

    def export(self, filename="", object_name=""):
        filename = self.file_path(
            filename=filename if filename else "{}.png".format(self.timestamp()),
            object_name=object_name,
        )

        qgis.utils.iface.mapCanvas().saveAsImage(filename)
        log(filename, icon="🖼️")

    def file_path(self, filename, object_name=""):
        return os.path.join(self.object_path(object_name), filename)

    def find_layer(self, layer_name):
        return QgsProject.instance().mapLayersByName(layer_name)

    def help(self, clear=False):
        if clear:
            self.clear()

        log("object", self.object_name, icon="📂")
        log("Q.clear()", "clear Python Console.")
        log("Q.create_video()", "create a video.")
        layer.help()
        if verbose:
            log("Q.export([filename],[object_name])", "export.")
            log("Q.list_of_layers()", "list of layers.")
            log("Q.load(filename,layer_name,template_name)", "load a layer.")
        log('Q.open("|<object-name>|layer|object|project")', "open.")
        project.help()
        if verbose:
            log("Q.refresh()", "refresh.")
            log("Q.reload()", "reload all layers.")
        log('Q.select("<object-name>")', "select <object-name>.")
        if verbose:
            log("Q.unload(layer_name)", "unload layer_name.")
        log('Q.upload("|<object-name>|layer|project|qgz")', "upload.")
        log("verbose=True|False", "set verbose state.")

        for app in self.app_list:
            app.help()

    def list_of_layers(self, aux=False):
        output = [
            layer_.name() for layer_ in QgsProject.instance().mapLayers().values()
        ]
        if not aux:
            output = [
                layer_name
                for layer_name in output
                if not layer_name.startswith("Google")
                and not layer_name.startswith("template")
            ]
        log(
            "{} layer(s){}".format(
                len(output),
                ": {}".format(", ".join(output)) if verbose else "",
            ),
            icon="🔎",
        )
        return output

    def load(
        self,
        filename,
        layer_name,
        template_name="",
        refresh=True,
    ):
        if len(self.find_layer(layer_name)) > 0:
            print(f"✅ {layer_name}")
            return True

        if filename.endswith(".geojson"):
            layer_ = QgsVectorLayer(filename, layer_name, "ogr")
        elif filename.endswith(".tif"):
            layer_ = QgsRasterLayer(filename, layer_name)
        else:
            log_error(f"cannot load {filename}.")
            return False

        if not layer_.isValid():
            log_error(f"invalid layer: {filename}.")
            return False

        QgsProject.instance().addMapLayer(layer_)

        if template_name:
            template_layer = self.find_layer(template_name)
            if not len(template_layer):
                log_error(f"template not found: {template_name}.")
                return False

            # https://gis.stackexchange.com/a/357206/210095
            source_style = QgsMapLayerStyle()
            source_style.readFromLayer(template_layer[0])
            source_style.writeToLayer(layer_)
            layer_.triggerRepaint()

        log(
            layer_name,
            template_name,
            icon="🎨",
        )

        if refresh:
            self.refresh()

    def object_path(self, object_name=""):
        output = os.path.join(
            abcli_object_root,
            object_name if object_name else self.object_name,
        )
        os.makedirs(output, exist_ok=True)
        return output

    def open(self, what="object"):
        self.open_folder(
            layer.path
            if what in "layer"
            else self.object_path() if what == "object" else project.path
        )

    def open_folder(self, path):
        if not path:
            log_error("path not found.")
            return

        log(path)
        os.system(f"open {path}")

    def refresh(self, deep=False):
        log("{}refresh.".format("deep" if deep else ""))
        if deep:
            # https://api.qgis.org/api/classQgsMapCanvas.html
            iface.mapCanvas().redrawAllLayers()
        else:
            iface.mapCanvas().refresh()

    def reload(self):
        # https://gis.stackexchange.com/a/449101/210095
        for layer_ in tqdm(QgsProject.instance().mapLayers().values()):
            layer_.dataProvider().reloadData()

    def select(self, object_name=""):
        self.object_name = object_name if object_name else self.timestamp()
        log(f"object_name: {self.object_name}", icon="📂")
        log(f"object_path: {self.object_path()}", icon="📂")

        os.makedirs(self.object_path(), exist_ok=True)

    def timestamp(self):
        return time.strftime(
            f"%Y-%m-%d-%H-%M-%S-{random.randrange(100000):05d}",
            time.localtime(time.time()),
        )

    def unload(self, layer_name, refresh=True):
        log(layer_name, icon="🗑️")

        for layer_ in self.find_layer(layer_name):
            QgsProject.instance().removeMapLayer(layer_.id())

        if refresh:
            self.refresh()

    def upload(self, object_name=""):
        seed(
            [
                "abcli",
                "upload",
                f"filename={project.name}.qgz" if object_name == "qgz" else "-",
                (
                    project.name
                    if object_name in ["project", "qgz", project]
                    else (
                        layer.object_name
                        if object_name in ["layer", layer]
                        else object_name if object_name else self.object_name
                    )
                ),
            ]
        )


QGIS = ABCLI_QGIS()

Q = QGIS
