from typing import List
import os
import re
import yaml


if not QGIS_is_live:
    from .application import BLUE_GEO_QGIS_APPLICATION
    from .help import Q_help
    from .logger import Q_log, Q_verbose, Q_clear
    from dependency import list_of_dependencies
    from .mock import QgsSettings
    from .testing import Q_test

    ABCLI_OBJECT_ROOT = ""

    BLUE_GEO_VERSION = "1.1.1"

Q_NAME = "Blue-GEO QGIS"
Q_ALIAS = "Q"


# https://qgis.org/pyqgis/master/core/QgsSettings.html#qgis.core.QgsSettings.allKeys
# https://docs.qgis.org/3.28/en/docs/pyqgis_developer_cookbook/settings.html
def Q_list_recent_projects() -> str:
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


def Q_QGIS_help():
    Q_log("Q_list_recent_projects()", "list recent projects.")


class ABCLI_QGIS:
    def __init__(self):
        self.app_list: List[BLUE_GEO_QGIS_APPLICATION] = []

    def add_app(self, app: BLUE_GEO_QGIS_APPLICATION):
        self.app_list += [app]

    def help(log):
        Q_log("Q.clear", "clear Python Console.")

    def intro(self):
        Q_log(self.version)
        Q_log('Type in "Q.help" for help.')

        for app in [app for app in self.app_list if app.name != "template"]:
            Q_log(f'Type in "{app.name}_help()" for help about {app.icon} {app.name}.')

    @property
    def version(self) -> str:
        return "{}-{} ({})".format(
            Q_NAME,
            BLUE_GEO_VERSION,
            Q_ALIAS,
        )

    # aliases

    @property
    def clear(self):
        Q_clear()

    @property
    def help(self):
        Q_help(clear=True)

    @property
    def test(self):
        Q_test()


QGIS = ABCLI_QGIS()
