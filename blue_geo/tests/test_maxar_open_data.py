import pytest
import datetime

from blue_geo.catalog.maxar_open_data.client import MaxarOpenDataClient


@pytest.mark.parametrize(
    ["collection_id", "is_valid_collection", "count"],
    [
        ["void", False, -1],
        ["WildFires-LosAngeles-Jan-2025", True, 3],
    ],
)
def test_maxar_open_data(
    collection_id: str,
    is_valid_collection: bool,
    count: int,
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
        count=count,
        log=True,
    )

    assert isinstance(list_of_items, list)
    assert len(list_of_items) > 0
    assert len(list_of_items) <= count

    item = list_of_items[0]

    datacube_id = client.get_datacube_id(
        item=item,
        collection_id=collection_id,
        log=True,
    )
    assert isinstance(datacube_id, str)
    assert datacube_id

    assert client.ingest(
        datacube_id=datacube_id,
        log=True,
    )

    assert client.get_filename(
        item=item,
        filename="103001010B9A1B00-visual.tif",
    )
