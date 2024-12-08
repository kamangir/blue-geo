from typing import Dict
import requests
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

from blueness import module
from blue_objects import host
from blue_objects import metadata, file, objects
from blue_geo import NAME
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)

name = "global-power-plant-database"

template_name = f"{name}-template-v1"


url: Dict[str, str] = {
    "dataset": "https://datasets.wri.org/datasets/global-power-plant-database",
    "research": "https://www.wri.org/research/global-database-power-plants",
    "metadata": "https://datasets.wri.org/api/3/action/resource_show?id=66bcdacc-3d0e-46ad-9271-a5a76b1853d2",
}

version = "v2"


def ingest(
    object_name: str,
    version: str = "v1",
    overwrite: bool = False,
    log: bool = True,
    verbose: bool = False,
) -> bool:
    full_object_name = f"{object_name}-{version}"

    logger.info(
        "{}.ingest({}) {}".format(
            NAME,
            full_object_name,
            ",".join((["overwrite"] if overwrite else [])),
        )
    )

    response = requests.get(url["metadata"])
    # https://chat.openai.com/c/6deb94d0-826a-48de-b5ef-f7d8da416c82
    # response.raise_for_status()
    if response.status_code // 100 != 2:
        logger.error("failed to access metadata.")
        return False
    if verbose:
        logger.info(response.json())

    download_url = response.json().get("result", {}).get("url", "")
    if not download_url:
        logger.error("failed to get download_url.")
        return False

    zip_filename = objects.path_of(
        download_url.split("/")[-1],
        full_object_name,
        create=True,
    )
    if not file.download(
        url=download_url,
        filename=zip_filename,
        log=log,
        overwrite=overwrite,
    ):
        return False

    if not host.unzip(zip_filename, log=log):
        return False

    success, df = file.load_dataframe(
        objects.path_of(
            "global_power_plant_database.csv",
            full_object_name,
        ),
        log=log,
    )
    if not success:
        return False

    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

    df = df.dropna(subset=["latitude", "longitude"])

    df["geometry"] = df.apply(
        lambda row: Point(row["longitude"], row["latitude"]),
        axis=1,
    )

    gdf = gpd.GeoDataFrame(
        df,
        geometry="geometry",
        crs="EPSG:4326",
    )

    if not file.save_geojson(
        objects.path_of(
            "global_power_plant_database.geojson",
            full_object_name,
        ),
        gdf,
        log=log,
    ):
        return False

    return metadata.post_to_object(
        full_object_name,
        "ingest",
        {
            "api-response": response.json(),
        },
    )
