if not QGIS_is_live:
    from .assets import Q_test_assets_object_references
    from ..objects import (
        Q_get_thing_name_or_path,
        Q_get_thing_name,
        Q_get_thing_path,
        Q_upload,
    )
    from ..logger import Q_log


def test_get_name_or_path(deep: bool = False):
    for what in Q_test_assets_object_references(deep=True):
        for property in ["object_name", "path"]:

            output = Q_get_thing_name_or_path(what, property)
            assert output
            Q_log(f"{what}.{property}: {output}")

        output = Q_get_thing_name(what)
        assert output
        Q_log(f"{what}.name: {output}")

        output = Q_get_thing_path(what)
        assert output
        Q_log(f"{what}.path: {output}")


def test_upload():
    for what in Q_test_assets_object_references(deep=True):
        Q_upload(what, dryrun=True)
