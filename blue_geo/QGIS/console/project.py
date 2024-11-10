import os

if not QGIS_is_live:
    from log import verbose, log
    from fileio import load_yaml


class ABCLI_QGIS_Project(object):
    def help(self):
        pass

    @property
    def filename(self):
        return QgsProject.instance().fileName()

    @property
    def list_of_layers(self):
        output = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
        if verbose:
            log(
                f"{len(output)} layer(s)",
                ", ".join(output) if verbose else "",
                icon="🔎",
            )
        return output

    @property
    def metadata(self):
        filename = os.path.join(self.path, "metadata.yaml")

        if not os.path.exists(filename):
            return {"error": f"{filename}: file not found."}

        return load_yaml(filename)

    @property
    def name(self):
        return QgsProject.instance().homePath().split(os.sep)[-1]

    @property
    def path(self):
        return QgsProject.instance().homePath()

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


project = ABCLI_QGIS_Project()
