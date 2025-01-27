import os
from typing import List

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
    version = "5.32.1"

    area = row["area"]
    damage = row["damage"]

    def seed(command: List[str]) -> List[str]:
        return [
            '<label for="seed">🌱</label>',
            '<input type="text" value="{}" id="seed" style="background-color: white; color: black; width: 100%;">'.format(
                " ".join(command)
            ),
        ]

    layer_path, layer_filename = os.path.split(layer_filename)
    object_name = layer_path.split(os.sep)[-1]
    object_root = os.sep.join(layer_path.split(os.sep)[:-1])
    is_analytics = "analytics.geojson" in layer_filename

    thumbnail_object_name = row["thumbnail_object"] if is_analytics else object_name

    thumbnail_filename = row["thumbnail"]
    thumbnail_full_filename = os.path.join(
        object_root,
        thumbnail_object_name,
        thumbnail_filename,
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
        ]
        + (
            ['<img src="file://{}" width=500 >'.format(thumbnail_full_filename)]
            if os.path.exists(thumbnail_full_filename)
            else seed(
                [
                    "abcli download",
                    f"filename={thumbnail_filename}",
                    thumbnail_object_name,
                ]
            )
        )
        + ["<hr/>"]
        + (
            seed(
                [
                    "palisades analytics render",
                    "building={},~download".format(row["building_id"]),
                    object_name,
                ]
            )
            if is_analytics
            else []
        )
        + [
            "<hr/>",
            '<p style="color: white; width: 500px">{}</p>'.format(
                " | ".join(
                    (
                        [
                            "analytics",
                            row["building_id"],
                        ]
                        if is_analytics
                        else []
                    )
                    + [
                        object_name,
                        f"template-{version}",
                    ]
                )
            ),
        ],
    )
