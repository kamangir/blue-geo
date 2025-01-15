from typing import Any, List
import pystac
import datetime
import pathlib

from blue_objects import objects, file

from blue_geo.logger.geoimage import log_geoimage
from blue_geo.logger import logger

URL = "https://maxar-opendata.s3.amazonaws.com/events/catalog.json"


class MaxarOpenDataClient:
    def __init__(
        self,
        verbose: bool = False,
    ):
        self.verbose = verbose

        self.catalog = pystac.Catalog.from_file(URL)

        if verbose:
            logger.info(self.catalog)

    def get_list_of_collections(
        self,
        log: bool = False,
    ) -> List[Any]:
        list_of_collections = [
            collection.id for collection in self.catalog.get_children()
        ]

        if self.verbose or log:
            logger.info(
                "{} collection(s): {}".format(
                    len(list_of_collections),
                    ", ".join(list_of_collections),
                )
            )

        return list_of_collections

    def get_collection(
        self,
        collection_id: str,
        log: bool = False,
    ) -> Any:
        collection = self.catalog.get_child(collection_id)

        if self.verbose or log:
            logger.info(collection)

        if (collection is None) or (not self.verbose and not log):
            return collection

        logger.info(list(collection.get_children()))

        for child in collection.get_children():
            logger.info(f"{child.id}")
            for item in child.get_items():
                logger.info(
                    "    {}: {}".format(
                        item.id,
                        item.properties["datetime"],
                    )
                )

        return collection

    def get_datacube_id(
        self,
        item: Any,
        collection_id: str,
        log: bool = False,
        verbose: bool = False,
    ) -> str:
        datacube_id = (
            f"datacube-Maxar-Open-Data-{collection_id}-{item.id.replace('/','-')}"
        )

        if log or self.verbose:
            logger.info(f"item: {item.id}")
            logger.info(item.to_dict())
            for asset in item.assets:
                logger.info("{}: {}".format(asset, item.assets[asset].href))

            logger.info(f"🧊 datacube-id: {datacube_id}")

        return datacube_id

    def ingest(
        self,
        datacube_id: str,
        asset_name: str = "visual",
        log: bool = True,
        verbose: bool = False,
        overwrite: bool = False,
    ) -> bool:
        if not datacube_id.startswith("datacube-Maxar-Open-Data-"):
            logger.error(f"Invalid datacube-id: {datacube_id}")
            return False

        list_of_collections = self.get_list_of_collections(log=verbose)

        candidate_collections = [
            collection_id
            for collection_id in list_of_collections
            if datacube_id.startswith(f"datacube-Maxar-Open-Data-{collection_id}-")
        ]
        if not candidate_collections:
            logger.error(f"collection not found: {datacube_id}.")
            return False
        if len(candidate_collections) > 1:
            logger.warning(
                "{} possible collection(s): {}".format(
                    len(candidate_collections), ", ".join(candidate_collections)
                )
            )

        collection_id = candidate_collections[0]
        logger.info(f"collection_id: {collection_id}")

        collection = self.get_collection(
            collection_id=collection_id,
            log=verbose,
        )
        if collection is None:
            return False

        item_id = datacube_id.split(f"datacube-Maxar-Open-Data-{collection_id}-", 1)[
            1
        ].replace("-", "/")
        logger.info(f"item_id: {item_id}")

        list_of_items = []
        for child in collection.get_children():
            list_of_items += [item for item in child.get_items() if item.id == item_id]
        if not list_of_items:
            logger.error(f"item not found: {item_id}.")
            return False
        if len(list_of_items) > 1:
            logger.warning(
                "{} possible item(s): {}".format(
                    len(list_of_items), ", ".join(list_of_items)
                )
            )
        item = list_of_items[0]
        logger.info(f"item: {item}.")

        if asset_name not in item.assets:
            logger.error(
                "{} not found in item.assets: {}".format(
                    asset_name,
                    ", ".join(list(item.assets.keys())),
                )
            )
            return False

        asset_relative_href = item.assets["visual"].href
        logger.info(f"asset_relative_href= {asset_relative_href}")

        if verbose:
            for link in item.links:
                logger.info("{}: {}".format(link.rel, link.href))

        root_href_candidates = [link.href for link in item.links if link.rel == "self"]
        if not root_href_candidates:
            logger.error(
                'cannot find "self" in {}.'.format(
                    ", ".join([link.rel for link in item.links])
                )
            )
            return False

        root_href = "/".join(root_href_candidates[0].split("/")[:-1])
        logger.info("root href: {}".format(root_href))

        asset_href = f"{root_href}/{asset_relative_href}"
        logger.info(f"asset_href: {asset_href}")

        filename = str(
            pathlib.Path(
                objects.path_of(
                    filename=asset_relative_href,
                    object_name=datacube_id,
                    create=True,
                )
            ).resolve()
        )
        logger.info(f"filename: {filename}")

        if not file.download(
            asset_href,
            filename=filename,
            overwrite=overwrite,
        ):
            return False

        return log_geoimage(
            filename=filename,
            object_name=datacube_id,
        )

    def query(
        self,
        collection_id: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        log: bool = False,
        verbose: bool = False,
    ) -> List[Any]:
        list_of_items = []

        collection = self.get_collection(
            collection_id=collection_id,
            log=verbose,
        )
        if collection is None:
            return list_of_items

        for child in collection.get_children():
            for item in child.get_items():
                item_date = datetime.datetime.strptime(
                    item.properties["datetime"], "%Y-%m-%d %H:%M:%SZ"
                )
                if start_date <= item_date <= end_date:
                    logger.info(f"{item.id} - {item_date}")

                    list_of_items += [item]

        if self.verbose or log:
            logger.info(f"{len(list_of_items):,} item(s).")

        return list_of_items
