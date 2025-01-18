import os

if not QGIS_is_live:
    from logger import Q_log, Q_log_error


def Q_path_exists(path: str) -> bool:
    return os.path.exists(path) and os.path.isdir(path)


def Q_open_path(
    path: str,
    dryrun: bool = False,
) -> bool:
    if not Q_path_exists(path):
        Q_log_error("path not found.")
        return False

    Q_log(path)

    if not dryrun:
        os.system(f"open {path}")

    return True
