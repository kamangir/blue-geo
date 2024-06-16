import pytest
from abcli.modules.objects import unique_object


@pytest.mark.parametrize(
    ["var1", "var2"],
    [
        ["value-11", "value-12"],
        ["value-21", "value-22"],
        ["value-31", "value-32"],
        ["value-41", "value-42"],
    ],
)
@pytest.mark.parametrize(
    ["var3", "var4"],
    [
        ["value-13", "value-14"],
        ["value-23", "value-24"],
        ["value-33", "value-34"],
        ["value-43", "value-44"],
    ],
)
def test_thing(
    var1: str,
    var2: str,
    var3: str,
    var4: str,
):
    object_name = unique_object()

    assert object_name
