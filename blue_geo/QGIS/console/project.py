import os
from tqdm import tqdm

if not QGIS_is_live:
    from .logger import Q_verbose, Q_log
    from .graphics import Q_refresh
    from .file_load import Q_load_yaml
    from .mock import QgsProject


class ABCLI_QGIS_Project(object):
    def help(self):
        pass

    def exists(
        self,
        layer_name: str,
        verbose: bool = True,
    ) -> bool:
        list_of_layers = self.get_layer(layer_name=layer_name)

        if len(list_of_layers) > 0:
            if verbose:
                Q_log(layer_name, icon="✅")
            return True

        return False

    @property
    def filename(self):
        return QgsProject.instance().fileName()

    def get_layer(self, layer_name):
        return QgsProject.instance().mapLayersByName(layer_name)

    @property
    def list_of_layers(
        self,
        aux: bool = False,
    ):
        output = [layer.name() for layer in QgsProject.instance().mapLayers().values()]

        if not aux:
            output = [
                layer_name
                for layer_name in output
                if not layer_name.startswith("Google")
                and not layer_name.startswith("template")
            ]

        if Q_verbose:
            Q_log(
                f"{len(output)} layer(s)",
                ", ".join(output),
                icon="🔎",
            )

        return output

    @property
    def metadata(self):
        filename = os.path.join(self.path, "metadata.yaml")

        if not os.path.exists(filename):
            return {"error": f"{filename}: file not found."}

        return Q_load_yaml(filename)

    @property
    def name(self):
        return QgsProject.instance().homePath().split(os.sep)[-1]

    @property
    def path(self):
        return QgsProject.instance().homePath()

    def reload(self):
        # https://gis.stackexchange.com/a/449101/210095
        for layer_ in tqdm(QgsProject.instance().mapLayers().values()):
            layer_.dataProvider().reloadData()

    def remove_layer(
        self,
        layer_name: str,
        refresh: bool = True,
    ):
        Q_log(layer_name, icon="🗑️")

        for layer_ in QgsProject.instance().mapLayersByName(layer_name):
            QgsProject.instance().removeMapLayer(layer_.id())
            Q_log(layer_name, icon="➖")

        if refresh:
            Q_refresh()

    def trim_empty_groups(self):
        root = QgsProject.instance().layerTreeRoot()
        groups_to_check = [root]

        while groups_to_check:
            group = groups_to_check.pop(0)
            children = group.children()
            empty = all(
                child.nodeType() == 0 and child.children() == [] for child in children
            )

            if empty and group != root:
                parent = group.parent()
                parent.removeChildNode(group)
            else:
                groups_to_check.extend(
                    [child for child in children if child.nodeType() == 0]
                )


Q_project = ABCLI_QGIS_Project()
