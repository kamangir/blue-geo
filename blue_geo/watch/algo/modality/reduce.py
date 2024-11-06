from typing import List, Dict
import glob
from tqdm import tqdm

from blueness import module
from blue_objects import file, objects
from blue_objects.graphics.gif import generate_animated_gif
from blue_objects.metadata import post_to_object

from blue_geo import NAME
from blue_geo.catalog.generic.generic.scope import raster_suffix
from blue_geo.watch.targets.target import Target
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def reduce_function(
    query_object_name: str,
    suffix: str,
    object_name: str,
    content_threshold: float = 0.5,
    list_of_suffix: List[str] = [],
) -> bool:
    success, target = Target.load(object_name)
    if not success:
        return success

    logger.info(
        "{}.reduce {}/{} @ {} -> {}{}".format(
            NAME,
            query_object_name,
            suffix,
            target.one_liner,
            object_name,
            " +{}".format(",".join(list_of_suffix)) if list_of_suffix else "",
        )
    )

    logger.info("loading metadata ...")
    frame_metadata: Dict[str, Dict] = {}
    list_of_files: List[str] = []
    bad_metadata: List[str] = []
    for filename in tqdm(
        sorted(
            glob.glob(
                objects.path_of(
                    "metadata-*.yaml",
                    object_name,
                )
            )
        )
    ):
        success, metadata_ = file.load_yaml(filename)
        if not success:
            bad_metadata.append(filename)
            continue

        if not "filename" in metadata_.get("map", {}):
            logger.info('no "filename" in metadata["map"]: {}.'.format(filename))
            bad_metadata.append(file.name_and_extension(filename))
            continue

        map_filename = metadata_["map"]["filename"]
        list_of_files += [map_filename]
        frame_metadata[map_filename] = metadata_

    if bad_metadata:
        logger.info("bad metadata: {}.".format(", ".join(bad_metadata)))

    bad_frames: List[str] = []
    low_content_frames: List[str] = []
    list_of_frames: List[str] = []
    for _, filename in enumerate(list_of_files):
        frame_metadata.setdefault(file.name_and_extension(filename), {})

        frame_content_ratio = (
            frame_metadata[file.name_and_extension(filename)]
            .get("map", {})
            .get("content_ratio", -1)
        )
        frame_is_usable = (
            frame_metadata[file.name_and_extension(filename)]
            .get("map", {})
            .get("usable", False)
        )
        if not frame_is_usable:
            bad_frames.append(file.name_and_extension(filename))
            continue

        frame_filename = objects.path_of(
            file.add_extension(filename, "png"),
            object_name,
        )

        frame_has_content = bool(frame_content_ratio >= content_threshold)
        logger.info(
            "{} / {}: content={:.03f} {} {:.03f}".format(
                "✅" if frame_has_content else "🛑",
                file.name_and_extension(filename),
                frame_content_ratio,
                ">=" if frame_has_content else "<",
                content_threshold,
            )
        )

        frame_metadata[file.name_and_extension(filename)].update(
            {
                "has_content": bool(frame_has_content),
            }
        )

        if not frame_has_content:
            low_content_frames.append(file.name_and_extension(filename))
            continue

        list_of_frames.append(frame_filename)
    if bad_frames:
        logger.error("{} bad frame(s).".format(len(bad_frames)))

    if not post_to_object(
        object_name,
        "reduce",
        {
            "algo": "modality",
            "bad_frames": bad_frames,
            "bad_metadata": bad_metadata,
            "frames": frame_metadata,
            "low_content_frames": low_content_frames,
            "list_of_files": [
                file.name_and_extension(filename) for filename in list_of_files
            ],
            "target": target.__dict__,
        },
    ):
        return False

    if not all(
        generate_animated_gif(
            list_of_frames,
            objects.path_of(
                "{}{}.gif".format(
                    object_name,
                    f"-{scale}X" if scale != 1 else "",
                ),
                object_name,
            ),
            frame_duration=1000,
            scale=scale,
        )
        for scale in [1, 2, 4]
    ):
        return False

    if list_of_suffix and not all(
        generate_animated_gif(
            [file.add_suffix(filename, frame_suffix) for filename in list_of_frames],
            objects.path_of(
                f"{object_name}-{frame_suffix}.gif",
                object_name,
            ),
            frame_duration=1000,
        )
        for frame_suffix in list_of_suffix
    ):
        return False

    return True
