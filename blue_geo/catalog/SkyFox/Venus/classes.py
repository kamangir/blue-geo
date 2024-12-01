from typing import List, Dict

from blue_objects import host, file, host

from blue_geo.catalog.SkyFox.classes import SkyFoxCatalog
from blue_geo.catalog.generic.generic.stac import STACDatacube
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo import env
from blue_geo.logger import logger


class SkyFoxVenusDatacube(STACDatacube):
    catalog = SkyFoxCatalog()

    collection = "venus-l2a"

    name = "Venus"

    QGIS_template = env.BLUE_GEO_QGIS_TEMPLATE_DATACUBE_SKYFOX_VENUS

    band_names: Dict[str, str] = {
        7: "red",
        4: "green",
        3: "blue",
    }

    @classmethod
    def band_index(cls, band_name: str) -> int:
        return {
            band_name: band_index for band_index, band_name in cls.band_names.items()
        }.get(band_name, -1)

    @staticmethod
    def band_suffix(
        band_index: int,
        product: str = "SRE",  # SRE | FRE
    ):
        return f"{product}_B{band_index}.tif"

    def generate(
        self,
        modality: str,
        overwrite: bool = False,
    ) -> str:
        product = ""
        if modality.startswith("rgb@"):
            modality, product = modality.split("@", 1)
        if not product:
            product = "SRE"

        # TODO: clean-up in the next refactor 🤦🏽
        if modality != "rgb":
            logger.error(f"{modality}: modality is not implemented.")
            return ""

        logger.info(
            "{}.generate({} : {})".format(
                self.__class__.__name__,
                modality,
                product,
            )
        )

        list_of_colors = ["red", "green", "blue"]

        rgb_filename: str = ""
        list_of_band_files: List[str] = []
        for color in list_of_colors:
            suffix = self.band_suffix(
                band_index=self.band_index(band_name=color),
                product=product,
            )

            candidates = self.list_of_files(DatacubeScope(suffix))
            if not candidates:
                logger.error(f"cannot find {suffix}.")
                return ""

            full_filename = self.full_filename(candidates[0])
            list_of_band_files += [full_filename]

            if not rgb_filename:
                rgb_filename = full_filename.replace(suffix, f"{product}_RGB.tif")

        if file.exists(rgb_filename) and not overwrite:
            logger.info(f"✅ {rgb_filename}")
            return ""

        return " ".join(
            [
                "gdal_merge.py",
                "-separate",
                f"-o {rgb_filename}",
            ]
            + list_of_band_files
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

        product: str = "FRE" if "_FRE_" in scope.contains else "SRE"

        output = scope.filter(
            [
                {
                    "filename": (value.href.split(f"{raw_datacube_id}/", 1)[1]),
                }
                for value in self.metadata["Item"].assets.values()
                if raw_datacube_id in value.href
            ],
            needed_for_rgb=lambda filename: any(
                filename.endswith(suffix)
                for suffix in [
                    self.band_suffix(
                        band_index,
                        product,
                    )
                    for band_index in [
                        self.band_index(color)
                        for color in [
                            "red",
                            "green",
                            "blue",
                        ]
                    ]
                ]
            ),
            verbose=verbose,
        )

        if scope.rgb:
            suffix = self.band_suffix(
                self.band_index("red"),
                product,
            )
            candidates = self.list_of_files(DatacubeScope(suffix))
            if candidates:
                rgb_filename = candidates[0].replace(suffix, f"{product}_RGB.tif")
                output += [rgb_filename]

        return output
