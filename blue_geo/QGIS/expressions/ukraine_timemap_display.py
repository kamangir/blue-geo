from qgis.core import *
from qgis.gui import *


@qgsfunction(args="auto", group="Custom", referenced_columns=[])
def ukraine_timemap_display(project_filename, id, date, description, feature, parent):
    """
    produce display text for a ukraine_timemap mapid.

    ukraine_timemap_display(
        "id",
        "description",
        "date",
    )
    """
    version = "1.9.1"

    return "<hr/>".join(
        [
            description,
            '{} | {} | #<a href="https://ukraine.bellingcat.com/?id={}">{}</a>'.format(
                project_filename.split(".")[0],
                date.toString("yyyy-MM-dd"),
                id,
                id,
            ),
            f"🇺🇦 ukraine timemap template {version}",
        ]
    )
