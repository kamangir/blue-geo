if not QGIS_is_live:
    from log import log, hr
    from blue_geo.QGIS.console.tests.test_QGIS import (
        test_logging,
        test_QGIS_export,
        test_QGIS_get_property,
        test_QGIS_open,
        test_QGIS_upload,
    )


list_of_tests = [
    test_logging,
    test_QGIS_export,
    test_QGIS_get_property,
    test_QGIS_open,
    test_QGIS_upload,
]


def test(deep: bool = False):
    log("testing ...")
    hr()

    for test_function in list_of_tests:
        log(f"testing {test_function} ...")
        test_function(deep=deep)
        hr()

    log(
        "ran {} test(s): {}".format(
            len(list_of_tests),
            ", ".join([test_function.__name__ for test_function in list_of_tests]),
        )
    )
