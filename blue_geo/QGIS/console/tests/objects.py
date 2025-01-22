if not QGIS_is_live:
    from .assets import Q_test_assets_object_references
    from ..objects import (
        Q_get_thing_name_or_path,
        Q_get_thing_name,
        Q_get_thing_path,
        Q_upload,
    )
    from ..logger import Q_log


def test_objects_get_name_or_path():
    for what in Q_test_assets_object_references:
        for property in ["name", "path"]:
            Q_log(f"testing {what}.{property}...")

            output = Q_get_thing_name_or_path(what, property)
            assert isinstance(output, str)

        Q_log(f"{what}.path...")
        output = Q_get_thing_name(what)
        assert isinstance(output, str)

        Q_log(f"{what}.name...")
        output = Q_get_thing_path(what)
        assert isinstance(output, str)


def test_objects_upload():
    for what in Q_test_assets_object_references:
        Q_upload(what, dryrun=True)
