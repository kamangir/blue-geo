if not QGIS_is_live:
    from ..graphics import Q_screenshot


def test_graphics_screenshot(deep: bool = False):
    Q_screenshot()
