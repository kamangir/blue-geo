from typing import List

if not QGIS_is_live:
    from ..QGIS import QGIS, Q_list_recent_projects


def test_QGIS():
    QGIS.intro()


def test_QGIS_aliases():
    QGIS.help

    QGIS.list_recent_projects

    QGIS.screenshot


def test_QGIS_list_recent_projects():
    list_recent_projects = Q_list_recent_projects()
    assert list_recent_projects, "No recent projects found"
    assert isinstance(list_recent_projects, str)
