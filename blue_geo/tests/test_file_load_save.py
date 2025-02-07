import pytest
from typing import Callable, Union, List

from blueness import module
from blue_options import string
from blue_objects import file, objects

from blue_geo.env import BLUE_GEO_TEST_OBJECT
from blue_geo import NAME
from blue_geo.file.load import (
    load_geodataframe,
    load_geojson,
)
from blue_geo.file.save import (
    save_geojson,
)
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


@pytest.fixture
def test_object():
    object_name = BLUE_GEO_TEST_OBJECT

    assert objects.download(object_name=object_name)

    yield object_name

    logger.info(f"deleting {NAME}.test_object ...")


@pytest.mark.parametrize(
    [
        "load_func",
        "filename",
        "save_func",
    ],
    [
        [
            load_geodataframe,
            "vancouver.geojson",
            save_geojson,
        ],
        [
            load_geojson,
            "vancouver.geojson",
            None,
        ],
    ],
)
def test_file_load_save(
    test_object,
    load_func: Callable,
    filename: str,
    save_func: Union[Callable, None],
):
    success, thing = load_func(
        objects.path_of(
            object_name=test_object,
            filename=filename,
        )
    )
    assert success

    if not save_func is None:
        assert save_func(
            file.add_suffix(
                objects.path_of(
                    object_name=test_object,
                    filename=filename,
                ),
                string.random(),
            ),
            thing,
        )
