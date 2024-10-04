from typing import List, Dict

from blue_objects import host, file, host

from blue_geo.catalog.SkyFox.classes import SkyFoxCatalog
from blue_geo.catalog.generic.generic.stac import STACDatacube
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo import env
from blue_geo.logger import logger

rgb_suffixes = [f"SRE_B{band_index}.tif" for band_index in [7, 4, 3]]


class SkyFoxVenusDatacube(STACDatacube):
    catalog = SkyFoxCatalog()

    collection = "venus-l2a"

    name = "Venus"

    QGIS_template = env.BLUE_GEO_QGIS_TEMPLATE_DATACUBE_SKYFOX_VENUS

    def generate(
        self,
        modality: str,
        overwrite: bool = False,
    ) -> str:
        # TODO: clean-up in the next refactor 🤦🏽
        if modality != "rgb":
            logger.error(f"{modality}: modality is not implemented.")
            return ""

        list_of_colors = ["red", "green", "blue"]

        filenames: Dict[str, str] = {}
        for suffix, color in zip(rgb_suffixes, list_of_colors):
            candidates = self.list_of_files(DatacubeScope(suffix))
            if not candidates:
                logger.error(f"cannot find {suffix}.")
                return ""

            filenames[color] = self.full_filename(candidates[0])

        rgb_filename = filenames["red"].replace(rgb_suffixes[0], "SRE_RGB.tif")
        if file.exists(rgb_filename) and not overwrite:
            logger.info(f"✅ {rgb_filename}")
            return ""

        return " ".join(
            [
                "gdal_merge.py",
                "-separate",
                f"-o {rgb_filename}",
            ]
            + [filenames[color] for color in list_of_colors]
        )

    def ingest_filename(
        self,
        filename: str,
        overwrite: bool = False,
        verbose: bool = True,
    ) -> bool:
        if super().ingest_filename(filename, overwrite, verbose):
            return True

        s3_uri = ""
        for item in self.metadata["Item"].assets.values():
            if item.href.endswith(filename):
                s3_uri = item.href
                break

        if not s3_uri:
            logger.info(f"{filename}: file not found.")
            return False

        # https://registry.opendata.aws/venus-l2a-cogs/
        return host.shell(
            "aws s3 cp --no-sign-request {} {}".format(
                s3_uri,
                self.full_filename(filename),
            ),
            log=verbose,
        )

    def list_of_files(
        self,
        scope: DatacubeScope = DatacubeScope("all"),
        verbose: bool = False,
    ) -> List[str]:
        raw_datacube_id = self.raw_datacube_id()

        output = scope.filter(
            [
                {
                    "filename": (value.href.split(f"{raw_datacube_id}/", 1)[1]),
                }
                for value in self.metadata["Item"].assets.values()
                if raw_datacube_id in value.href
            ],
            needed_for_rgb=lambda filename: any(
                filename.endswith(suffix) for suffix in rgb_suffixes
            ),
            verbose=verbose,
        )

        if scope.rgb:
            suffix = rgb_suffixes[0]
            candidates = self.list_of_files(DatacubeScope(suffix))
            if candidates:
                rgb_filename = candidates[0].replace(suffix, "SRE_RGB.tif")
                output += [rgb_filename]

        return output
