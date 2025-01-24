import math
from qgis.core import *
from qgis.gui import *

# version 2.2.1


@qgsfunction(args="auto", group="Custom", referenced_columns=[])
def palisades_label(row, feature, parent):
    """
    Produce label text for a palisades mapid.

    palisades_label(row)
    """

    area = row["area"]
    damage = row["damage"]

    return "{:,} sq. m{}".format(
        area,
        " - {:.1f} %".format(100 * damage) if damage > 0 else "",
    )
