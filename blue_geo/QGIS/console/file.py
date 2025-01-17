import os
import shutil

if not QGIS_is_live:
    from logger import log_error, log


def Q_copy_file(
    source_filename: str,
    destination_filename: str,
) -> bool:
    try:
        # https://stackoverflow.com/a/8858026
        # better choice: copy2
        shutil.copyfile(source_filename, destination_filename)
    except:
        log_error(
            "Q_copy_file({},{}): failed.".format(
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


def Q_add_extension(filename: str, extension: str) -> str:
    filename, _ = os.path.splitext(filename)

    return f"{filename}.{extension}"


def Q_get_file_extension(filename: str) -> str:
    return os.path.splitext(filename)[1][1:]


def Q_get_file_name(filename: str) -> str:
    _, filename = os.path.split(filename)

    return filename if "." not in filename else ".".join(filename.split(".")[:-1])


def Q_get_file_name_and_extension(filename: str) -> str:
    return os.path.basename(filename)


def file_path(filename: str) -> str:
    return os.path.split(filename)[0]
