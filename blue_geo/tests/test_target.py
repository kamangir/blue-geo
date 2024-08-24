import os
from abcli import file, path
from blue_geo.target import Target


def test_load_targets():
    targets = Target(
        os.path.join(
            file.path(__file__),
            "../watch/targets.yaml",
        )
    )

    assert targets.items
