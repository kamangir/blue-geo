if not QGIS_is_live:
    from logger import Q_log, Q_hr

    from tests.application import test_template_application
    from tests.graphics import test_graphics_screenshot
    from tests.help import test_help
    from tests.logger import test_logging
    from tests.objects import test_objects_get_name_or_path, test_objects_upload
    from tests.QGIS import test_QGIS, test_QGIS_aliases, test_QGIS_list_recent_projects
    from tests.string import test_timestamp


list_of_tests = [
    test_graphics_screenshot,
    test_help,
    test_logging,
    test_objects_get_name_or_path,
    test_objects_upload,
    test_QGIS,
    test_QGIS_aliases,
    test_QGIS_list_recent_projects,
    test_template_application,
    test_timestamp,
]


def Q_test():
    description: str = "{} test(s): {}".format(
        len(list_of_tests),
        ", ".join([test_function.__name__ for test_function in list_of_tests]),
    )

    Q_log(f"running {description} ...")
    Q_hr()

    for test_function in list_of_tests:
        Q_log(f"testing {test_function} ...")
        test_function()
        Q_hr()

    Q_log(f"ran {description}.", icon="✅")
