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


def test_load_targets(target_list):
    assert target_list.targets

    for target in target_list.targets.values():
        assert isinstance(target, Target)

    for target in ["chilcotin-river-landslide", "elkhema"]:
        assert target in target_list.targets
