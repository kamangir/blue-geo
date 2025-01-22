from typing import List
import os
import re
import yaml


if not QGIS_is_live:
    from dependency import list_of_dependencies
    from .application import BLUE_GEO_QGIS_APPLICATION
    from .help import Q_help
    from .file_save import Q_save_yaml
    from .graphics import Q_screenshot
    from .logger import Q_log, Q_verbose, Q_clear
    from .mock import QgsSettings
    from .objects import Q_get_thing_path, Q_upload, Q_open
    from .path import Q_open_path
    from .project import Q_project
    from .project import Q_layer
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

    list_of_projects = [
        filename.split(f"{ABCLI_OBJECT_ROOT}/", 1)[1].split("/")[0]
        for filename in list_of_filenames
        if ABCLI_OBJECT_ROOT in filename
    ]

    for filename in list_of_filenames:
        list_of_projects += list_of_dependencies(
            filename=filename,
            ABCLI_OBJECT_ROOT=ABCLI_OBJECT_ROOT,
            verbose=Q_verbose,
        )

    list_of_projects = list(set(list_of_projects))

    Q_save_yaml(
        os.path.join(ABCLI_OBJECT_ROOT, "QGIS-recent.yaml"),
        list_of_projects,
    )

    Q_log(f"{len(list_of_projects)} recent project(s).")

    return ",".join(list_of_projects)


class ABCLI_QGIS:
    def __init__(self):
        self.app_list: List[BLUE_GEO_QGIS_APPLICATION] = []

    def add_app(self, app: BLUE_GEO_QGIS_APPLICATION):
        self.app_list += [app]

    def help_(self):
        Q_log("Q.clear", "clear Python Console.")
        Q_log("Q.list_recent_projects", "list recent projects.")
        Q_log("Q.open", "open project in Finder.")
        Q_log("Q.screenshot", "screenshot.")
        Q_log("Q.test", "test Q.")
        Q_log("Q.upload", "upload project.")

    def intro(self):
        Q_log(self.version)

        for app in [app for app in self.app_list if app.name != "template"]:
            Q_log(f"{app.icon} {app.name}")

        Q_log('Type in "Q.help" for help.')

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
        Q_clear(log=False)

    @property
    def help(self):
        Q_help(clear=True)

    @property
    def layer(self):
        return Q_layer

    @property
    def list_recent_projects(self):
        Q_list_recent_projects()

    @property
    def open(self):
        Q_open(thing=Q_project)

    @property
    def project(self):
        return Q_project

    @property
    def screenshot(self):
        Q_screenshot()

    @property
    def test(self):
        Q_test()

    @property
    def upload(self):
        Q_upload(thing=Q_project)


QGIS = ABCLI_QGIS()

Q = QGIS
