from typing import Any, List, Tuple
import pystac
import datetime
import pathlib
from tqdm import tqdm
from shapely.geometry import Point, Polygon

from blue_objects import objects, file, metadata

from blue_geo import env
from blue_geo.logger.geoimage import log_geoimage
from blue_geo.catalog.generic.generic.scope import raster_suffix
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
    ) -> List[str]:
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
            f"datacube-maxar_open_data-{collection_id}-{item.id.replace('/','-')}"
        )

        if log or self.verbose:
            logger.info(f"item: {item.id}")
            logger.info(item.to_dict())
            for asset in item.assets:
                logger.info("{}: {}".format(asset, item.assets[asset].href))

            logger.info(f"🧊 datacube-id: {datacube_id}")

        return datacube_id

    def parse_datacube_id(
        self,
        datacube_id: str,
        log: bool = True,
        verbose: bool = False,
    ) -> Tuple[bool, str, str]:
        collection_id: str = ""
        item_id: str = ""

        if not datacube_id.startswith("datacube-maxar_open_data-"):
            if log:
                logger.error(f"Invalid datacube-id: {datacube_id}")
            return False, collection_id, item_id

        list_of_collections = self.get_list_of_collections(log=verbose)

        candidate_collections = [
            collection_id
            for collection_id in list_of_collections
            if datacube_id.startswith(f"datacube-maxar_open_data-{collection_id}-")
        ]
        if not candidate_collections:
            if log:
                logger.error(f"collection not found: {datacube_id}.")
            return False, collection_id, item_id
        if len(candidate_collections) > 1:
            if log:
                logger.warning(
                    "{} possible collection(s): {}".format(
                        len(candidate_collections), ", ".join(candidate_collections)
                    )
                )

        collection_id = candidate_collections[0]
        if log:
            logger.info(f"collection_id: {collection_id}")

        suffix = datacube_id.split(f"datacube-maxar_open_data-{collection_id}-", 1)[1]
        if "-DERIVED-" in suffix:
            suffix = suffix.split("-DERIVED-", 1)[0]

        item_id = suffix.replace("-", "/")
        if log:
            logger.info(f"item_id: {item_id}")

        return True, collection_id, item_id

    def get_filename(self, item, filename: str) -> str:
        return "{}-{}".format(
            item.id.replace("/", "-"),
            (filename.split("./", 1)[1] if filename.startswith("./") else filename),
        )

    def get_item(
        self,
        datacube_id: str,
        log: bool = False,
        read_from_cache: bool = env.MAXAR_OPEN_DATA_CLIENT_CACHE_ITEMS,
        write_to_cache: bool = env.MAXAR_OPEN_DATA_CLIENT_CACHE_ITEMS,
    ) -> Tuple[bool, Any]:
        cache_filename = objects.path_of(
            object_name=datacube_id,
            filename="item.bin",
        )

        if read_from_cache and file.exists(cache_filename):
            success, item = file.load(cache_filename, ignore_error=True)
            if success:
                return success, item

        success, collection_id, item_id = self.parse_datacube_id(
            datacube_id=datacube_id,
            log=log,
            verbose=log,
        )
        if not success:
            return success, None

        collection = self.get_collection(
            collection_id=collection_id,
            log=log,
        )
        if collection is None:
            return False, None

        list_of_items = []
        for child in collection.get_children():
            list_of_items += [item for item in child.get_items() if item.id == item_id]
        if not list_of_items:
            logger.error(f"item not found: {item_id}.")
            return False, None
        if len(list_of_items) > 1:
            logger.warning(
                "{} possible item(s): {}".format(
                    len(list_of_items), ", ".join(list_of_items)
                )
            )
        item = list_of_items[0]
        if log:
            logger.info(f"item: {item}.")

        if write_to_cache:
            file.save(cache_filename, item)

        return True, item

    def ingest(
        self,
        datacube_id: str,
        list_of_assets: List[str] = ["visual"],
        log: bool = True,
        verbose: bool = False,
        overwrite: bool = False,
    ) -> bool:
        success, item = self.get_item(
            datacube_id=datacube_id,
            log=verbose,
        )
        if not success:
            return success

        for asset_name in tqdm(list_of_assets):
            if asset_name not in item.assets:
                logger.error(
                    "{} not found in item.assets: {}".format(
                        asset_name,
                        ", ".join(list(item.assets.keys())),
                    )
                )
                success = False
                continue

            logger.info(f"ingesting {asset_name} ...")

            asset_relative_href = item.assets[asset_name].href
            logger.info(f"asset_relative_href= {asset_relative_href}")

            if verbose:
                for link in item.links:
                    logger.info("{}: {}".format(link.rel, link.href))

            root_href_candidates = [
                link.href for link in item.links if link.rel == "self"
            ]
            if not root_href_candidates:
                logger.error(
                    'cannot find "self" in {}.'.format(
                        ", ".join([link.rel for link in item.links])
                    )
                )
                success = False
                continue

            root_href = "/".join(root_href_candidates[0].split("/")[:-1])
            logger.info("root href: {}".format(root_href))

            asset_href = f"{root_href}/{asset_relative_href}"
            logger.info(f"asset_href: {asset_href}")

            suffixed_filename = self.get_filename(
                item=item,
                filename=asset_relative_href,
            )
            full_filename = str(
                pathlib.Path(
                    objects.path_of(
                        filename=suffixed_filename,
                        object_name=datacube_id,
                        create=True,
                    )
                ).resolve()
            )
            logger.info(f"filename: {full_filename}")

            if not file.download(
                asset_href,
                filename=full_filename,
                overwrite=overwrite,
            ):
                success = False
                continue

            if any(
                suffixed_filename.endswith(suffix) for suffix in raster_suffix
            ) and not log_geoimage(
                filename=suffixed_filename,
                object_name=datacube_id,
            ):
                success = False
                continue

        if not metadata.post_to_object(
            datacube_id,
            "item_info",
            item.to_dict(),
        ):
            success = False

        return success

    def query(
        self,
        collection_id: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        lat: float = -1,
        lon: float = -1,
        radius: float = env.MAXAR_OPEN_DATA_CLIENT_QUERY_RADIUS,
        count: int = -1,
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

        for child in tqdm(collection.get_children()):
            for item in child.get_items():
                item_date = datetime.datetime.strptime(
                    item.properties["datetime"],
                    (
                        "%Y-%m-%dT%H:%M:%SZ"
                        if "T" in item.properties["datetime"]
                        else "%Y-%m-%d %H:%M:%SZ"
                    ),
                )
                if start_date > item_date or item_date > end_date:
                    continue

                if lat != -1 and lon != -1:
                    polygon = Polygon(item.geometry["coordinates"][0])
                    point = Point(lon, lat)
                    if not point.within(polygon.buffer(radius)):
                        continue

                logger.info(f"{item.id} - {item_date}")
                list_of_items += [item]

                if count != -1 and len(list_of_items) >= count:
                    break

            if count != -1 and len(list_of_items) >= count:
                break

        if self.verbose or log:
            logger.info(f"{len(list_of_items):,} item(s).")

        return list_of_items
