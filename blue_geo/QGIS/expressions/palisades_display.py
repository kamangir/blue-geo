import os

from qgis.core import *
from qgis.gui import *


@qgsfunction(args="auto", group="Custom", referenced_columns=[])
def palisades_display(layer_filename, row, feature, parent):
    """
    Produce display text for a palisades mapid.

    palisades_display(
        layer_property(@layer,'path'),
        attributes($currentfeature)
    )
    """
    version = "5.10.1"

    area = row["area"]
    damage = row["damage"]

    layer_path = os.path.split(layer_filename)[0]
    thumbnail = os.path.join(layer_path, row["thumbnail"])

    object_name = layer_path.split(os.sep)[-1]

    return "\n".join(
        [
            '<p style="color: {};">area: {:,.0f} sq. m, damage: {:.1f}%'.format(
                "green" if damage == 0 else "yellow" if damage < 0.1 else "red",
                area,
                damage * 100,
            ),
            "<hr/>",
            '<img src="file://{}" width=500 >'.format(thumbnail),
            "<hr/>",
            '<p style="color: white; width: 500px">{}</p>'.format(
                " | ".join(
                    [
                        object_name,
                        f"template version {version}",
                    ]
                )
            ),
        ]
    )
