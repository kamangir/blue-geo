import yaml
from typing import List, Any

if not QGIS_is_live:
    from .logger import Q_log


def Q_save_text(
    filename: str,
    text: List[str],
    log: bool = True,
):
    with open(filename, "w") as fp:
        fp.writelines([string + "\n" for string in text])

    if log:
        Q_log(
            "Q_save_text: {:,} line(s) -> {}".format(
                len(text),
                filename,
            )
        )


def Q_save_yaml(
    filename: str,
    data: Any,
    log=True,
):
    with open(filename, "w") as file:
        yaml.dump(data, file)

    Q_log(f"-> {filename}")
