if not QGIS_is_live:
    from QGIS import QGIS
    from apps.vanwatch import ROOFAI_QGIS_APPLICATION_VANWATCH
    from apps.template import ROOFAI_QGIS_APPLICATION_TEMPLATE
    from apps.ukraine_timemap import ROOFAI_QGIS_APPLICATION_UKRAINE_TIMEMAP


vanwatch = ROOFAI_QGIS_APPLICATION_VANWATCH()
QGIS.add_application(vanwatch)

template = ROOFAI_QGIS_APPLICATION_TEMPLATE()
QGIS.add_application(template)

ukraine_timemap = ROOFAI_QGIS_APPLICATION_UKRAINE_TIMEMAP()
ukraine = ukraine_timemap
QGIS.add_application(ukraine_timemap)

QGIS.intro()
