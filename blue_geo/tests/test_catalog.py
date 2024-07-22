import pytest
from blue_geo.tests import assets
from blue_geo.datacube.catalogs import catalog_of


@pytest.mark.parametrize(
    ["datacube_id", "expected_success", "expected_catalog"],
    [
        [
            [
                asset
                + [
                    "generic",
                ]
                for asset in assets.datacube_generic_parse_datacube_id
            ]
            + [
                asset
                + [
                    "firms_area",
                ]
                for asset in assets.datacube_firms_area_parse_datacube_id
            ]
        ],
    ],
)
def test_catalog_of(
    datacube_id: str,
    expected_success: bool,
    expected_catalog: str,
):
    success, catalog = catalog_of(datacube_id)

    assert success == expected_success
    if success:
        assert catalog == expected_catalog
    else:
        assert catalog == "unknown-catalog"
