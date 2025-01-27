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
    version = "5.29.1"

    area = row["area"]
    damage = row["damage"]

    layer_path, layer_filename = os.path.split(layer_filename)
    object_name = layer_path.split(os.sep)[-1]
    object_root = os.sep.join(layer_path.split(os.sep)[:-1])
    is_analytics = "analytics.geojson" in layer_filename

    thumbnail_object_name = row["thumbnail_object"] if is_analytics else object_name

    thumbnail_filename = os.path.join(
        object_root,
        thumbnail_object_name,
        row["thumbnail"],
    )

    return "\n".join(
        [
            '<p style="color: {};">{}</p>'.format(
                "green" if damage == 0 else "yellow" if damage < 0.1 else "red",
                " | ".join(
                    [
                        "area: {:,.0f} sq. m".format(area),
                        "damage: {:.1f}%{}".format(
                            100 * damage,
                            (
                                " +- {:.1f}%".format(100 * row["damage_std"])
                                if is_analytics
                                else ""
                            ),
                        ),
                    ]
                    + (
                        ["{} observation(s)".format(row["observation_count"])]
                        if is_analytics
                        else []
                    )
                ),
            ),
            "<hr/>",
            '<img src="file://{}" width=500 >'.format(thumbnail_filename),
            "<hr/>",
        ]
        + (
            [
                '    <label for="seed">🌱</label>',
                '<input type="text" value="{}" id="seed" style="background-color: white; color: black; width: 100%;">'.format(
                    " ".join(
                        [
                            "palisades analytics render",
                            "building={},~download".format(row["building_id"]),
                            object_name,
                        ]
                    )
                ),
                "<hr/>",
            ]
            if is_analytics
            else []
        )
        + [
            '<p style="color: white; width: 500px">{}</p>'.format(
                " | ".join(
                    (
                        [
                            "analytics",
                            row["building_id"],
                        ]
                        if is_analytics
                        else [""]
                    )
                    + [
                        object_name,
                        f"template-{version}",
                    ]
                )
            ),
        ]
    )
