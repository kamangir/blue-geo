import os


class ABCLI_QGIS_Project(object):
    def help(self):
        pass

    @property
    def name(self):
        return QgsProject.instance().homePath().split(os.sep)[-1]

    @property
    def path(self):
        return QgsProject.instance().homePath()


project = ABCLI_QGIS_Project()
