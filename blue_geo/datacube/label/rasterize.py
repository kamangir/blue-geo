from typing import Dict
import numpy as np
import rasterio
from rasterio.features import rasterize
from tqdm import tqdm

from blueness import module
from blue_objects import objects, file
from blue_objects.metadata import post_to_object

from blue_geo import NAME
from blue_geo.catalog import get_datacube
from blue_geo.catalog.generic.generic.scope import DatacubeScope
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


def rasterize_the_label(
    datacube_id: str,
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.rasterize_the_label: {datacube_id}")

    datacube = get_datacube(datacube_id)

    list_of_files = datacube.list_of_files(scope=DatacubeScope("rgb"))
    if not list_of_files:
        logger.error("cannot find a reference file.")
        return False

    reference_filename = list_of_files[0]
    logger.info(f"reference: {reference_filename}")

    label_filename = objects.path_of(
        filename="label.shp",
        object_name=datacube_id,
    )
    success, label_polygons = file.load_geodataframe(label_filename)
    if not success:
        return success
    logger.info(
        "label: {} - {} polygon(s)".format(
            file.name_and_extension(label_filename),
            len(label_polygons),
        )
    )

    success, label_template_polygons = file.load_geodataframe(
        objects.path_of(
            filename="template/label.shp",
            object_name=datacube_id,
        )
    )
    if not success:
        return success
    list_of_classes = sorted(list(set(label_template_polygons["class"].tolist())))
    if "background" in list_of_classes:
        list_of_classes = ["background"] + [
            class_name for class_name in list_of_classes if class_name != "background"
        ]
    logger.info(
        "{} class(es): {}".format(
            len(list_of_classes),
            ", ".join(list_of_classes),
        )
    )

    class_pixel_count: Dict[str, int] = {
        class_name: 0 for class_name in list_of_classes
    }
    with rasterio.open(
        objects.path_of(
            filename=reference_filename,
            object_name=datacube_id,
        )
    ) as src:
        label_image = np.zeros(src.shape, dtype=np.uint8)

        transform = src.transform
        meta = src.meta
        meta["count"] = 1

        label_polygons = label_polygons.to_crs(src.crs)

        for _, row in tqdm(label_polygons.iterrows()):
            class_name = row["class"]

            class_index = list_of_classes.index(class_name)

            polygon_mask = rasterize(
                [(row.geometry, class_index)],
                out_shape=src.shape,
                fill=0,
                transform=transform,
                all_touched=True,
                dtype=np.uint8,
            )

            pixel_count = int(np.sum(polygon_mask != 0))
            class_pixel_count[class_name] += pixel_count
            if verbose:
                logger.info(
                    "#{} {}: {:,} pixel(s)".format(
                        class_index, class_name, pixel_count
                    ),
                )

            label_image = np.maximum(label_image, polygon_mask)

    for class_name in list_of_classes:
        logger.info(f"{class_name}: {class_pixel_count[class_name]:,} pixel(s)")

    with rasterio.open(
        objects.path_of(
            filename=file.add_suffix(reference_filename, "label"),
            object_name=datacube_id,
        ),
        "w",
        **meta,
    ) as dst:
        dst.write(label_image, 1)

    return post_to_object(
        datacube_id,
        "rasterize",
        {
            "counts": class_pixel_count,
            "label_count": len(label_polygons),
            "label_filename": file.name_and_extension(label_filename),
            "list_of_classes": list_of_classes,
            "reference_filename": reference_filename,
        },
    )
