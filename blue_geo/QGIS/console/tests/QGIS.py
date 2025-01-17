from typing import List

if not QGIS_is_live:
    from ..logger import log, log_error, verbose, hr
    from ..QGIS import QGIS
    from ..layer import layer
    from ..project import project


def open_upload_test_assets(
    deep: bool = False,
) -> List[str]:
    output = [
        project,
        "project",
        "qgz",
        #
        layer,
        "layer",
        #
        "object",
        object,
    ]

    if not deep:
        output = [output[0]]

    return output


def test_QGIS_logging(deep: bool = False):
    QGIS.clear()

    QGIS.intro()


def test_QGIS_screenshot(deep: bool = False):
    QGIS.screenshot()


def test_QGIS_get_property(deep: bool = False):
    for property in ["object_name", "path"]:
        for what in open_upload_test_assets(deep=True):
            output = QGIS.get_property(what, property)
            assert output

            log(f"{what}.{property}: {output}")


def test_QGIS_open(deep: bool = False):
    for what in open_upload_test_assets(deep=deep):
        QGIS.open(what)


def test_QGIS_upload(deep: bool = False):
    for what in open_upload_test_assets(deep=deep):
        QGIS.upload(what)

        upload(what)
