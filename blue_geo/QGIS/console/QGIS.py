import os
import re
import yaml
import time
import random
from tqdm import tqdm


if not QGIS_is_live:
    from .application import Q_app_list
    from .logger import Q_clear, Q_hr, Q_log, Q_log_error, Q_verbose
    from .seed import Q_seed
    from dependency import list_of_dependencies
    from .graphics import Q_refresh
    from .mock import QgsProject, QgsSettings

    ABCLI_OBJECT_ROOT = ""


class ABCLI_QGIS(object):
    def Q_help(self, clear=False):
        Q_log("Q.list_recent_projects()", "list recent projects.")

    # https://qgis.org/pyqgis/master/core/QgsSettings.html#qgis.core.QgsSettings.allKeys
    # https://docs.qgis.org/3.28/en/docs/pyqgis_developer_cookbook/settings.html
    def list_recent_projects(self):
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


QGIS = ABCLI_QGIS()
