import os
from typing import Any, Tuple, Dict, List

from blueness import module
from blue_objects import file, objects, path
from blue_objects.metadata import post_to_object

from blue_geo import NAME
from blue_geo.catalog.generic.classes import GenericCatalog, VoidCatalog
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


class GenericDatacube:
    name = "generic"

    catalog = GenericCatalog()

    datacube_id = ""

    metadata: Any = None

    query_args: Dict[str, Dict] = {
        "arg": {
            "default": "value",
            "help": "<value>",
        },
    }

    QGIS_template = "unknown-template"

    def __init__(self, datacube_id: str = ""):
        self.datacube_id = datacube_id
        if self.datacube_id:
            self.update_metadata()

    @property
    def description(self) -> str:
        return "{}.{}@{}[{}]:".format(
            NAME,
            self.__class__.__name__,
            self.catalog.name,
            self.datacube_id,
        )

    def full_filename(self, filename: str) -> str:
        return objects.path_of(filename, self.datacube_id, create=True)

    def ingest(
        self,
        dryrun: bool = False,
        overwrite: bool = False,
        scope: str = "metadata",
    ) -> Tuple[bool, Any]:
        logger.info(
            "{}.{}.ingest({}): {} @ {}".format(
                NAME,
                self.__class__.__name__,
                ",".join(
                    [
                        item
                        for item in ["dryrun" if dryrun else ""]
                        + ["overwrite" if overwrite else ""]
                        if item
                    ]
                ),
                scope,
                self.datacube_id,
            )
        )

        return True, None

    # returns True if ingest is complete.
    def ingest_filename(
        self,
        filename: str,
        overwrite: bool = False,
        verbose: bool = False,
    ) -> bool:
        item_filename = self.full_filename(filename)

        assert path.create(file.path(item_filename))

        if item_filename.endswith(os.sep):
            return True

        if not overwrite and file.exists(item_filename):
            logger.info(f"✅ {item_filename}")
            return True

        logger.info("ingesting {} ...".format(filename))

        return False

    def list_of_files(
        self,
        scope: DatacubeScope = DatacubeScope("all"),
        verbose: bool = False,
    ) -> List[str]:
        return []

    @classmethod
    def parse_datacube_id(cls, datacube_id: str) -> Tuple[
        bool,
        Dict[str, Any],
    ]:
        # datacube-<catalog-name>-<args>
        segments = datacube_id.split("-") + ["", ""]

        return (
            segments[0] == "datacube" and segments[1] == cls.catalog.name,
            {},
        )

    @property
    def path(self) -> str:
        return objects.object_path(self.datacube_id)

    @classmethod
    def query(cls, object_name: str) -> bool:
        logger.info(f"🔎 {cls.__name__}.query -> {object_name}")

        return post_to_object(object_name, "datacube_id", [])

    def update_metadata(self, verbose: bool = False) -> bool:
        if verbose:
            logger.info(f"{self.description}.update_metadata()")

        return True


class VoidDatacube(GenericDatacube):
    name = "void"
    catalog = VoidCatalog()
