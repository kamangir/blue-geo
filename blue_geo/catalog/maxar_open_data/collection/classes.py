from typing import Tuple, Dict, Any, List
import datetime

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
            "help": "WildFires-LosAngeles-Jan-2025 | ...",
        },
        "lat": {
            "type": float,
            "default": -1,
            "help": "<51.83>",
        },
        "lon": {
            "type": float,
            "default": -1,
            "help": "<-122.78>",
        },
        "radius": {
            "type": float,
            "default": env.MAXAR_OPEN_DATA_CLIENT_QUERY_RADIUS,
            "help": f"<{env.MAXAR_OPEN_DATA_CLIENT_QUERY_RADIUS}>",
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
        "count": {
            "default": -1,
            "type": int,
            "help": "-1 | <value>",
        },
    }

    QGIS_template = env.BLUE_GEO_QGIS_TEMPLATE_MAXAR_OPEN_DATA

    def ingest(
        self,
        dryrun: bool = False,
        overwrite: bool = False,
        scope: str = "metadata",
    ) -> Tuple[bool, Any]:
        success, output = super().ingest(dryrun, overwrite, scope)
        if not success:
            return success, output

        return (
            self.catalog.client.ingest(
                datacube_id=self.datacube_id,
                list_of_assets=self.list_of_files(
                    scope=DatacubeScope(scope),
                    return_asset_names=True,
                ),
            ),
            {},
        )

    def list_of_files(
        self,
        scope: DatacubeScope = DatacubeScope("all"),
        return_asset_names: bool = False,
        verbose: bool = False,
    ) -> List[str]:
        success, item = self.catalog.client.get_item(
            datacube_id=self.datacube_id,
            log=verbose,
        )
        if not success:
            return []

        list_of_assets = [
            {
                "filename": self.catalog.client.get_filename(
                    item=item,
                    filename=asset.href,
                ),
                "asset_name": asset_name,
            }
            for asset_name, asset in item.assets.items()
        ]

        output = scope.filter(
            list_of_assets,
            needed_for_rgb=lambda filename: filename.endswith("-visual.tif"),
            is_rgb=lambda filename: filename.endswith("-visual.tif"),
            verbose=verbose,
        )

        if return_asset_names:
            output = [
                asset["asset_name"]
                for asset in list_of_assets
                if asset["filename"] in output
            ]

        return output

    @classmethod
    def parse_datacube_id(cls, datacube_id: str) -> Tuple[
        bool,
        Dict[str, Any],
    ]:
        success, _ = super().parse_datacube_id(datacube_id)
        if not success:
            return False, {}

        success, item_id, collection_id = cls.catalog.client.parse_datacube_id(
            datacube_id=datacube_id,
            log=False,
        )
        return success, {
            "item_id": item_id,
            "collection_id": collection_id,
        }

    @classmethod
    def query(
        cls,
        object_name: str,
        collection_id: str,
        start_date: str,
        end_date: str,
        lat: float = -1,
        lon: float = -1,
        radius: float = env.MAXAR_OPEN_DATA_CLIENT_QUERY_RADIUS,
        count: int = -1,
    ) -> bool:
        logger.info(f"🔎 {cls.__name__}.query -> {object_name}")

        list_of_items = cls.catalog.client.query(
            collection_id=collection_id,
            start_date=datetime.datetime.strptime(start_date, "%Y-%m-%d"),
            end_date=datetime.datetime.strptime(end_date, "%Y-%m-%d"),
            lat=lat,
            lon=lon,
            radius=radius,
            count=count,
            log=True,
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
