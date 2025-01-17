if not QGIS_is_live:
    from ..logger import hr, log, log_error, log_warning, verbose


def test_logging(deep: bool = False):
    hr()
    hr(length=5)

    log("some message")
    log("some message", "some note")
    log("some message", "some note", "🔍")

    log_error("this is a test, don't panic! 😁")

    log_warning("this is a test, don't panic! 😁")

    assert isinstance(verbose, bool)
