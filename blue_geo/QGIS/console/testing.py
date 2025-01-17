if not QGIS_is_live:
    from logger import log, hr

    from tests.alias import test_aliases

    # from tests.layer import test_layer...
    from tests.logger import test_logging
    from tests.QGIS import (
        test_QGIS_get_property,
        test_QGIS_logging,
        test_QGIS_open,
        test_QGIS_screenshot,
        test_QGIS_upload,
    )


list_of_tests = [
    test_aliases,
    test_logging,
    test_QGIS_get_property,
    test_QGIS_logging,
    test_QGIS_open,
    test_QGIS_screenshot,
    test_QGIS_upload,
]


def Q_test(deep: bool = False):
    description: str = "{} test(s): {}".format(
        len(list_of_tests),
        ", ".join([test_function.__name__ for test_function in list_of_tests]),
    )

    log(f"running {description} ...")
    hr()

    for test_function in list_of_tests:
        log(f"testing {test_function} ...")
        test_function(deep=deep)
        hr()

    log(f"ran {description}.")
