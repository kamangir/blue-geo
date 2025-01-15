from typing import Tuple, Dict, Any, List
import datetime
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

from blue_objects import file, objects
from blue_objects import metadata
from blue_objects.metadata import post_to_object

from blue_geo.catalog.maxar_open_data.classes import MaxarOpenDataCatalog
from blue_geo.catalog.generic import GenericDatacube
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo import env
from blue_geo.logger import logger


class MaxarOpenDataDatacube(GenericDatacube):
    name = "collection"

    catalog = MaxarOpenDataCatalog()

    query_args = {
        "collection_id": {
            "default": "WildFires-LosAngeles-Jan-2025",
            "help": "<@maxar list>",
        },
        "start_date": {
            "default": (datetime.datetime.now() - datetime.timedelta(days=14)).strftime(
                "%Y-%m-%d"
            ),
            "help": "<yyyy-mm-dd>",
        },
        "end_date": {
            "default": (datetime.datetime.now()).strftime("%Y-%m-%d"),
            "help": "<yyyy-mm-dd>",
        },
    }

    QGIS_template = env.BLUE_GEO_QGIS_TEMPLATE_MAXAR_OPEN_DATA

    @classmethod
    def query(
        cls,
        object_name: str,
        collection_id: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
    ) -> bool:
        logger.info(f"🔎 {cls.__name__}.query -> {object_name}")

        list_of_items = cls.catalog.client.query(
            collection_id=collection_id,
            start_date=start_date,
            end_date=end_date,
        )

        list_of_datacube_ids: List[str] = [
            cls.catalog.client.get_datacube_id(
                item=item,
                collection_id=collection_id,
            )
            for item in list_of_items
        ]

        logger.info(f"{len(list_of_datacube_ids)} datacubes(s) found.")
        for index, datacube_id in enumerate(list_of_datacube_ids):
            logger.info(f"🧊 {index+1:02}: {datacube_id}")

        return post_to_object(object_name, "datacube_id", list_of_datacube_ids)
