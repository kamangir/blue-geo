if not QGIS_is_live:
    from logger import Q_log, Q_hr

    from tests.alias import test_aliases
    from tests.application import test_template_application
    from tests.graphics import test_graphics_screenshot
    from tests.logger import test_logging
    from tests.string import test_timestamp


list_of_tests = [
    test_aliases,
    test_graphics_screenshot,
    test_logging,
    test_template_application,
    test_timestamp,
]


def Q_test(deep: bool = False):
    description: str = "{} test(s): {}".format(
        len(list_of_tests),
        ", ".join([test_function.__name__ for test_function in list_of_tests]),
    )

    Q_log(f"running {description} ...")
    Q_hr()

    for test_function in list_of_tests:
        Q_log(f"testing {test_function} ...")
        test_function(deep=deep)
        Q_hr()

    Q_log(f"ran {description}.", icon="✅")
