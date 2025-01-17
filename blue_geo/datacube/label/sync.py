from blueness import module
import glob
from tqdm import tqdm

from blue_objects import objects, file

from blue_geo import NAME
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


def sync_the_label(
    datacube_id: str,
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.sync_the_label({datacube_id})")

    label_filename = objects.path_of(
        object_name=datacube_id,
        filename="label.shp",
    )
    if file.exists(label_filename):
        logger.info(f"✅ {label_filename}")
        return True

    template_filename = objects.path_of(
        object_name=datacube_id,
        filename="template/label.shp",
    )
    if not file.exists(template_filename):
        logger.error(f"template not found: {template_filename}.")
        return False

    from blue_objects.storage import instance as storage

    if storage.exists(object_name=f"{datacube_id}/label.shp"):
        logger.info(f"☁️ {label_filename}")

        for filename in tqdm(glob.glob(file.add_extension(template_filename, "*"))):
            extension = file.extension(filename)

            if not storage.download_file(
                object_name=f"bolt/{datacube_id}/label.{extension}",
                filename="object",
            ):
                return False

        return True

    logger.info("copying the template...")
    for filename in tqdm(glob.glob(file.add_extension(template_filename, "*"))):
        if not file.copy(
            filename,
            file.add_extension(
                label_filename,
                file.extension(filename),
            ),
        ):
            return False

    return True
