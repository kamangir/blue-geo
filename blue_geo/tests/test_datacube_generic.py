from blue_geo.datacube.types import GenericDatacube


def test_datacube_generic():
    datacube = GenericDatacube()

    assert datacube.datacube_id
