import pytest

from blue_objects import objects
from blue_objects.env import ABCLI_OBJECT_ROOT

from blue_geo.env import BLUE_GEO_WATCH_TARGET_LIST
from blue_geo.QGIS.dependency import list_of_dependencies


@pytest.mark.parametrize(
    ["object_name"],
    [[BLUE_GEO_WATCH_TARGET_LIST]],
)
def test_parse_datacube_id(
    object_name: str,
):
    assert objects.download(
        object_name=object_name,
        filename=f"{object_name}.qgz",
    )

    output = list_of_dependencies(
        objects.path_of(filename=f"{object_name}.qgz", object_name=object_name),
        ABCLI_OBJECT_ROOT,
    )

    assert isinstance(output, list)
    assert output
    assert object_name in output
