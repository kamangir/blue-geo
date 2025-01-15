import pytest
import datetime

from blue_geo.maxar_open_data.classes import MaxarOpenDataClient


@pytest.mark.parametrize(
    ["collection_id", "is_valid_collection"],
    [
        ["void", False],
        ["WildFires-LosAngeles-Jan-2025", True],
    ],
)
def test_maxar_open_data(
    collection_id: str,
    is_valid_collection: bool,
):
    client = MaxarOpenDataClient()

    client.get_list_of_collections()

    collection = client.get_collection(collection_id)
    if not is_valid_collection:
        assert collection is None
        return

    assert collection is not None

    list_of_items = client.query(
        collection_id=collection_id,
        start_date=datetime.datetime(2025, 1, 10),
        end_date=datetime.datetime(2025, 1, 13),
        log=True,
    )

    assert isinstance(list_of_items, list)
    assert len(list_of_items) > 0

    datacube_id = client.get_datacube_id(
        list_of_items[0],
        collection_id=collection_id,
        log=True,
    )
    assert isinstance(datacube_id, str)
    assert datacube_id

    assert client.ingest(
        datacube_id=datacube_id,
        log=True,
    )
