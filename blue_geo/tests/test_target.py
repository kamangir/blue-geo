import os
import pytest
from blue_geo.watch.targets.classes import Target, TargetList


@pytest.fixture
def target_list():
    return TargetList(download=True)


@pytest.mark.parametrize(
    ["catalog_name", "collection", "expected_target"],
    [
        ["SkyFox", "Venus", "Leonardo"],
        ["EarthSearch", "sentinel_2_l1c", "burning-man-2024"],
    ],
)
def test_target_list(
    catalog_name: str,
    collection: str,
    expected_target: str,
    target_list: TargetList,
):
    list_of_targets = target_list.get_list(
        catalog_name=catalog_name,
        collection=collection,
    )

    assert expected_target in list_of_targets


def test_targets_load(target_list: TargetList):
    assert target_list.targets

    for target in target_list.targets.values():
        assert isinstance(target, Target)

    for target in ["chilcotin-river-landslide", "elkhema"]:
        assert target in target_list.targets
