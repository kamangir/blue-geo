import os
import pytest
from blue_geo.watch.targets import Target, TargetList


@pytest.fixture
def target_list():
    return TargetList(
        os.path.join(
            os.path.dirname(__file__),
            "../watch/targets.yaml",
        )
    )


@pytest.mark.parametrize(
    ["description"],
    [
        ["void"],
        ["elkhema"],
        ["chilcotin-river-landslide"],
        ["datetime=2024-07-30/2024-08-15,lat=51.83,lon=-122.78"],
    ],
)
def test_get_target(target_list, description: str):
    target = target_list.get_target(description)
    assert isinstance(target, Target)


def test_load_targets(target_list):
    assert target_list.targets
    for target in target_list.targets:
        assert isinstance(target, Target)

    for target in ["chilcotin-river-landslide", "elkhema"]:
        assert target in target_list.targets
