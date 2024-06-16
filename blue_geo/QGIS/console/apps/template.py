if not QGIS_is_live:
    from application import ROOFAI_QGIS_APPLICATION


class ROOFAI_QGIS_APPLICATION_TEMPLATE(ROOFAI_QGIS_APPLICATION):
    def __init__(self):
        super().__init__("template", "🌀")

    def help(self):
        self.log(
            "template.func(var)",
            "func.",
        )

    def func(self, var: str = "🪄"):
        self.log(var)

