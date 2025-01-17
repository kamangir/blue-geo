import os
import re
import yaml
import time
import random
from tqdm import tqdm


if not QGIS_is_live:
    from logger import Q_clear, Q_hr, Q_log, Q_log_error, Q_verbose
    from layer import layer
    from project import project
    from seed import Q_seed
    from dependency import list_of_dependencies
    from .graphics import Q_refresh
    from .mock import QgsProject, QgsSettings

    ABCLI_OBJECT_ROOT = ""


class ABCLI_QGIS(object):
    def __init__(self):
        self.app_list = []

    def add_application(self, app):
        self.app_list += [app]

    def get_layer(self, layer_name: str):
        candidate_layers = QgsProject.instance().mapLayersByName(layer_name)

        return candidate_layers[0] if len(candidate_layers) else None

    def help(self, clear=False):
        if clear:
            Q_clear()

        Q_log("clear()", "clear Python Console.")

        layer.help()

        Q_log("Q_screenshot([filename],[object_name])", "screenshot.")

        Q_log("Q.list_of_layers()", "list of layers.")
        Q_log("Q.load(filename,layer_name,template_name)", "load a layer.")

        Q_log('Q.open(" | <object-name> | layer | project")', "open.")

        project.help()

        Q_log("Q_refresh()", "refresh.")
        Q_log("Q.reload()", "reload all layers.")

        Q_log("Q.unload(layer_name)", "unload layer_name.")

        Q_log('upload(" | <object-name> | layer | project | qgz")', "upload.")

        Q_log("Q_test(deep=True)", f"test Q.")

        Q_log("Q_verbose  = True|False", "set Q's verbose state.")

        for app in self.app_list:
            app.help()

    def layer_exists(
        self,
        layer_name,
        do_log: bool = False,
    ):
        for layer_name_ in project.list_of_layers:
            if layer_name_.startswith(layer_name):
                if do_log:
                    Q_log(
                        layer_name,
                        layer_name_ if Q_verbose else "",
                        icon="✅",
                    )
                return True
        return False

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
        Q_log(
            "{} layer(s){}".format(
                len(output),
                ": {}".format(", ".join(output)) if Q_verbose else "",
            ),
            icon="🔎",
        )
        return output

    # https://qgis.org/pyqgis/master/core/QgsSettings.html#qgis.core.QgsSettings.allKeys
    # https://docs.qgis.org/3.28/en/docs/pyqgis_developer_cookbook/settings.html
    def recent(self):
        settings = QgsSettings()

        list_of_filenames = [
            settings.value(key)
            for key in settings.allKeys()
            if re.match(r"UI/recentProjects/(\d+)/path", key)
        ]

        output = [
            filename.split(f"{ABCLI_OBJECT_ROOT}/", 1)[1].split("/")[0]
            for filename in list_of_filenames
            if ABCLI_OBJECT_ROOT in filename
        ]

        for filename in list_of_filenames:
            output += list_of_dependencies(filename, ABCLI_OBJECT_ROOT, Q_verbose)

        output = list(set(output))

        filename = os.path.join(ABCLI_OBJECT_ROOT, "QGIS-recent.yaml")
        with open(filename, "w") as file:
            yaml.dump(output, file)
        Q_log(f"-> {filename}")

        return ",".join(output)

    def reload(self):
        # https://gis.stackexchange.com/a/449101/210095
        for layer_ in tqdm(QgsProject.instance().mapLayers().values()):
            layer_.dataProvider().reloadData()

    def remove_layer(
        self,
        layer_name: str,
        refresh: bool = True,
    ):
        for layer_ in QgsProject.instance().mapLayersByName(layer_name):
            QgsProject.instance().removeMapLayer(layer_.id())
            Q_log(layer_name, icon="➖")

        if refresh:
            Q_refresh()

    def unload(
        self,
        layer_name: str,
        refresh: bool = True,
    ):
        Q_log(layer_name, icon="🗑️")

        for layer_ in self.get_layer(layer_name):
            QgsProject.instance().removeMapLayer(layer_.id())

        if refresh:
            Q_refresh()


QGIS = ABCLI_QGIS()
