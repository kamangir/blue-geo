from typing import List

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
