from blue_geo.catalog.SkyFox.classes import SkyFoxCatalog


def test_SkyFoxCatalog_token():
    success, token = SkyFoxCatalog.get_new_token()
    assert success
    assert token
