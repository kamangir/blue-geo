Q_verbose = False

QGIS_is_live = True

if not QGIS_is_live:
    from .QGIS import QGIS
    from .seed import Q_seed
    from .mock import iface


def Q_clear(
    log: bool = True,
    dryrun: bool = False,
):
    if not dryrun:
        # https://gis.stackexchange.com/a/480025/250728
        from qgis.PyQt.QtWidgets import QDockWidget

        consoleWidget = iface.mainWindow().findChild(QDockWidget, "PythonConsole")
        consoleWidget.widget().console.clearButton.trigger()

    QGIS.intro()

    Q_seed(
        "clear",
        log=log,
        dryrun=dryrun,
    )


def Q_hr(length: int = 3):
    print(length * ". .. ... .. ")


def Q_log(message, note="", icon="🌐"):
    print(
        "{} {}{}".format(
            icon,
            (
                (f"{message:.<40}" if len(message) < 38 else f"{message}\n   {40*'.'}")
                if note
                else message
            ),
            note,
        )
    )


def Q_log_error(message):
    Q_log(message, icon="❗️")


def Q_log_warning(message):
    Q_log(message, icon="❓")
