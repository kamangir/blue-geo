import os
from typing import Any, Tuple, Dict, List
import numpy as np

from blueness import module
from blue_options import string
from blue_objects import file, objects, path
from blue_objects.metadata import post_to_object
from blue_objects.logger.image import log_image_hist
from blue_objects.env import ABCLI_OBJECT_ROOT

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

    def generate(
        self,
        modality: str,
        overwrite: bool = False,
    ) -> str:
        return ""

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
        verbose: bool = True,
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

    @staticmethod
    def load_modality(
        filename: str,
        modality: str,
        ignore_error: bool = False,
        log: bool = False,
        verbose: bool = False,
    ) -> Tuple[bool, np.ndarray, Dict[str, Any]]:
        success, frame, frame_file_metadata = file.load_geoimage(
            filename,
            ignore_error=ignore_error,
            log=log,
        )
        if not success:
            return success, frame, frame_file_metadata

        frame = np.transpose(frame, (1, 2, 0))

        frame_range = (float(np.min(frame)), float(np.max(frame)))
        logger.info(
            "frame: {} : {}".format(
                string.pretty_shape_of_matrix(frame),
                frame_range,
            )
        )

        if frame.shape[2] == 6:
            frame = frame[:, :, [0, 2, 4]]
        elif frame.shape[2] > 3:
            frame = frame[:, :, :3]

        if log:
            if not log_image_hist(
                image=frame,
                range=frame_range,
                header=[
                    f"{frame_range[0]:.2f} .. {frame_range[1]:.2f}",
                ],
                footer=(
                    filename.split(f"{ABCLI_OBJECT_ROOT}/", 1)[1].split(os.sep)
                    if ABCLI_OBJECT_ROOT in filename
                    else [file.name_and_extension(filename)]
                ),
                filename=file.add_suffix(
                    file.add_extension(filename, "png"), "histogram"
                ),
            ):
                success = False

        return success, frame, frame_file_metadata

    @property
    def raw(self) -> str:
        return "{}.{}: {}".format(
            self.catalog.name,
            self.name,
            self.datacube_id,
        )

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

    def raw_datacube_id(
        self,
        datacube_id: str = "",  # to enable upstream modifications
    ) -> str:
        datacube_id = self.datacube_id if not datacube_id else datacube_id

        segments = datacube_id.split("-", 3)

        output = segments[3] if len(segments) >= 4 else ""

        if "-DERIVED-" in output:
            output = output.split("-DERIVED-", 1)[0]

        return output

    def update_metadata(self, verbose: bool = False) -> bool:
        if verbose:
            logger.info(f"{self.description}.update_metadata()")

        return True


class VoidDatacube(GenericDatacube):
    name = "void"
    catalog = VoidCatalog()
