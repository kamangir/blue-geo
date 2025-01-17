Q_verbose = False

QGIS_is_live = True

if not QGIS_is_live:
    from .application import Q_app_list
    from .seed import Q_seed
    from .mock import iface

    BLUE_GEO_VERSION = "1.1.1"

NAME = "Q"


def Q_clear():
    # https://gis.stackexchange.com/a/480025/250728
    from qgis.PyQt.QtWidgets import QDockWidget

    consoleWidget = iface.mainWindow().findChild(QDockWidget, "PythonConsole")
    consoleWidget.widget().console.clearButton.trigger()

    Q_intro()

    Q_seed("clear")


def Q_hr(length: int = 3):
    print(length * ". .. ... .. ")


def Q_intro():
    Q_log(
        "{}-{}: {}".format(
            NAME,
            BLUE_GEO_VERSION,
            ", ".join([f"{app.name} {app.icon}" for app in Q_app_list.app_list]),
        )
    )
    Q_log('Type in "Q_help()" for help.')

    for app in [app for app in Q_app_list.app_list if app.name != "template"]:
        Q_log(f'Type in "{app.name}_help()" for help about {app.icon} {app.name}.')


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


def Q_log_error(message, note=""):
    Q_log(message, note, icon="❗️")


def Q_log_warning(message, note=""):
    Q_log(message, note, icon="❓")
