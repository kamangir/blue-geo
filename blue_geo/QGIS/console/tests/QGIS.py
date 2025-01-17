from typing import List

if not QGIS_is_live:
    from ..QGIS import QGIS


def test_QGIS_list_of_projects(deep: bool = False):
    list_of_projects = QGIS.list_of_projects()
    assert list_of_projects, "No projects found"
    assert isinstance(list_of_projects, str)
