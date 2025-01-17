import pytest

from blue_objects import file, objects
from blue_geo.watch.targets.target import Target
from blue_geo.watch.targets.target_list import TargetList


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
    assert target_list.list_of_targets

    assert target_list.test()

    assert target_list.object_name

    assert file.exists(target_list.filename())

    list_of_targets = target_list.get_list(
        catalog_name=catalog_name,
        collection=collection,
    )

    assert expected_target in list_of_targets


def test_target_list_load(target_list: TargetList):
    assert target_list.list_of_targets

    for target in target_list.list_of_targets.values():
        assert isinstance(target, Target)

    for target in ["chilcotin-river-landslide", "elkhema"]:
        assert target in target_list.list_of_targets


def test_target_list_get(
    target_list: TargetList,
):
    target = target_list.get("bellingcat-2024-09-27-nagorno-karabakh")
    assert target.query_args["datetime"] == "2024-05-01/2024-09-01"

    target = target_list.get(
        "bellingcat-2024-09-27-nagorno-karabakh-test",
        including_versions=False,
    )
    assert not "count" in target.query_args

    target = target_list.get("bellingcat-2024-09-27-nagorno-karabakh-void")
    assert not "count" in target.query_args

    target = target_list.get("bellingcat-2024-09-27-nagorno-karabakh")
    assert target.query_args["count"] == 30

    target = target_list.get("bellingcat-2024-09-27-nagorno-karabakh-test")
    assert target.query_args["count"] == 2


def test_target_list_save(
    target_list: TargetList,
):
    object_name = objects.unique_object()

    assert target_list.save(object_name)

    assert file.exists(
        objects.path_of(
            filename="target/shape.geojson",
            object_name=object_name,
        )
    )


@pytest.mark.parametrize(
    ["catalog_name"],
    [
        [""],
        ["maxar_open_data"],
    ],
)
def test_target_list_for_catalog(
    catalog_name: str,
):
    target_list = TargetList(
        catalog=catalog_name,
        download=True,
    )

    assert len(target_list.list_of_targets) > 0
