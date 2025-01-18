if not QGIS_is_live:
    from ..apps.template import template


def test_template_application():
    template.log("some message")

    template.help_()

    template.func(var="testing...")
