import os
import shutil

if not QGIS_is_live:
    from logger import Q_log_error, Q_log


def Q_add_extension(filename: str, extension: str) -> str:
    filename, _ = os.path.splitext(filename)

    return f"{filename}.{extension}"


def Q_file_exists(filename: str) -> bool:
    return os.path.isfile(filename)


def Q_get_file_extension(filename: str) -> str:
    return os.path.splitext(filename)[1][1:]


def Q_get_file_name(filename: str) -> str:
    _, filename = os.path.split(filename)

    return filename if "." not in filename else ".".join(filename.split(".")[:-1])


def Q_get_file_name_and_extension(filename: str) -> str:
    return os.path.basename(filename)


def Q_get_file_path(filename: str) -> str:
    return os.path.split(filename)[0]


def Q_copy_file(
    source_filename: str,
    destination_filename: str,
) -> bool:
    try:
        # https://stackoverflow.com/a/8858026
        # better choice: copy2
        shutil.copyfile(source_filename, destination_filename)
    except Exception as e:
        Q_log_error(e)
        return False

    Q_log(f"{source_filename} -> {destination_filename}")
    return True
