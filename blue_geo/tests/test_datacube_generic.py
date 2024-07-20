from abcli.modules.objects import unique_object
from blue_geo.datacube.generic import GenericDatacube


def test_datacube_generic():
    object_name = unique_object()

    datacube = GenericDatacube()

    assert datacube.description

    success, _ = datacube.ingest(object_name)
    assert success

    assert datacube.datacube_id
