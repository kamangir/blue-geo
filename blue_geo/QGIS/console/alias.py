if not QGIS_is_live:
    from .QGIS import QGIS
    from .logger import Q_clear
    from .objects import Q_upload

Q = QGIS


def clear():
    Q_clear()


def upload(
    thing: str = "",
    dryrun: bool = False,
):
    Q_upload(
        thing=thing,
        dryrun=dryrun,
    )
