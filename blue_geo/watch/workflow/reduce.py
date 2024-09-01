from typing import List, Dict
import glob
from tqdm import tqdm
import numpy as np
from blueness import module
from abcli import string
from abcli import file
from abcli.plugins.graphics.signature import add_signature
from abcli.plugins.graphics.gif import generate_animated_gif
from abcli.modules.host import signature as host_signature
from abcli.modules.objects import signature as header
from abcli.plugins.metadata import post_to_object
from abcli.modules import objects
from blue_geo import NAME, VERSION
from blue_geo import NAME as BLUE_GEO_NAME
from notebooks_and_scripts import NAME as NBS_NAME, VERSION as NBS_VERSION
from blue_geo.watch.workflow.common import load_watch
from blue_geo.logger import logger


NAME = module.name(__file__, NAME)


def reduce_function(
    query_object_name: str,
    suffix: str,
    object_name: str,
    content_threshold: float = 0.5,
) -> bool:
    success, target, list_of_files = load_watch(object_name)
    if not success:
        return success

    logger.info(
        "{}.reduce {}/{} @ {} -{} file(s)-> {}".format(
            NAME,
            query_object_name,
            suffix,
            target,
            len(list_of_files),
            object_name,
        )
    )

    logger.info("loading metadata ...")
    frame_metadata: Dict[str, Dict] = {}
    bad_metadata: List[str] = []
    for filename in tqdm(
        glob.glob(
            objects.path_of(
                "metadata-*.yaml",
                object_name,
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

        frame_metadata[metadata_["map"]["filename"]] = metadata_
    if bad_metadata:
        logger.info("bad metadata: {}.".format(", ".join(bad_metadata)))

    bad_frames: List[str] = []
    low_content_frames: List[str] = []
    list_of_frames: List[str] = []
    for index, filename in enumerate(list_of_files):
        frame_metadata.setdefault(file.name_and_extension(filename), {})

        datacube_id = (
            frame_metadata[file.name_and_extension(filename)]
            .get("map", {})
            .get("datacube_id", "unknown")
        )

        success, frame = file.load_image(filename)
        if not success:
            bad_frames.append(file.name_and_extension(filename))
            continue

        frame_fp32 = frame.astype(np.float32).flatten() / 255.0
        frame_fp32 = frame_fp32[frame_fp32 > 0.0]
        frame_fp32 = frame_fp32[frame_fp32 < 1.0]
        frame_content_ratio = len(frame_fp32) / frame.size

        frame_has_content = bool(frame_content_ratio > content_threshold)
        logger.info(
            "{} {} / {} @ {}: content={:.03f} <?> {:.03f}".format(
                "✅" if frame_has_content else "🛑",
                datacube_id,
                file.name_and_extension(filename),
                string.pretty_shape_of_matrix(frame),
                frame_content_ratio,
                content_threshold,
            )
        )

        frame_metadata[file.name_and_extension(filename)].update(
            {
                "content": float(frame_content_ratio),
                "has_content": bool(frame_has_content),
                "shape": list(frame.shape),
            }
        )

        if not frame_has_content:
            low_content_frames.append(file.name_and_extension(filename))
            continue

        frame = add_signature(
            frame,
            header=[
                " | ".join(
                    header(
                        "{} / {}".format(
                            datacube_id,
                            file.name_and_extension(filename),
                        ),
                        object_name,
                    )
                    + [
                        "{:05.1f}%".format(frame_content_ratio * 100.0),
                        "{:03d} / {:03d}".format(index, len(list_of_files)),
                    ]
                ),
            ],
            footer=[
                str(target),
                " | ".join(
                    [f"{BLUE_GEO_NAME}.{VERSION}"]
                    + [f"{NBS_NAME}.{NBS_VERSION}"]
                    + host_signature()
                ),
            ],
            word_wrap=False,
        )

        frame_filename = file.set_extension(filename, "png")
        if not file.save_image(frame_filename, frame):
            bad_frames.append(frame_filename)
        else:
            list_of_frames.append(frame_filename)
    if bad_frames:
        logger.error("{} bad frame(s).".format(len(bad_frames)))

    if not post_to_object(
        object_name,
        "reduce",
        {
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

    return all(
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
        for scale in [1, 2]
    )
