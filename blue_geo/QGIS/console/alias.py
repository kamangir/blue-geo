if not QGIS_is_live:
    from .QGIS import QGIS
    from .logger import Q_log
    from .logger import Q_clear
    from .objects import Q_upload

Q = QGIS


def upload(
    thing: str = "",
    dryrun: bool = False,
):
    Q_upload(
        thing=thing,
        dryrun=dryrun,
    )


def Q_alias_help():
    Q_log('upload(" | <object-name> | layer | project | qgz")', "upload.")
