import os
import yaml
import shutil

if not QGIS_is_live:
    from log import log_error, log


def copy_file(
    source_filename: str,
    destination_filename: str,
) -> bool:
    try:
        # https://stackoverflow.com/a/8858026
        # better choice: copy2
        shutil.copyfile(source_filename, destination_filename)
    except:
        log_error(
            "copy_file({},{}): failed.".format(
                source_filename,
                destination_filename,
            )
        )
        return False

    log(
        "{} -> {}".format(
            source_filename,
            destination_filename,
        )
    )
    return True


def file_extension(filename: str) -> str:
    return os.path.splitext(filename)[1][1:]


def file_name(filename: str) -> str:
    _, filename = os.path.split(filename)

    return filename if "." not in filename else ".".join(filename.split(".")[:-1])


def file_name_and_extension(filename: str) -> str:
    return os.path.basename(filename)


def file_path(filename: str) -> str:
    return os.path.split(filename)[0]


def load_yaml(filename):
    with open(filename, "r") as file:
        return yaml.safe_load(file)


def file_with_extension(filename: str, extension: str) -> str:
    filename, _ = os.path.splitext(filename)

    return f"{filename}.{extension}"
