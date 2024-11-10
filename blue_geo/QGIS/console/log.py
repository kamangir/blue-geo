verbose = False

QGIS_is_live = True


def log(message, note="", icon="🌐"):
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


def log_error(message, note=""):
    log(message, note, icon="❗️")


def log_warning(message, note=""):
    log(message, note, icon="❓")
