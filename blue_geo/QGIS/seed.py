from blue_objects.env import ABCLI_OBJECT_ROOT

from blue_geo import VERSION


def generate_seed() -> str:
    list_of_modules = [
        "log",
        "project",
        "layer",
        "application",
        "seed",
        "QGIS",
        "apps/vanwatch",
        "apps/template",
        "apps/ukraine_timemap",
        "main",
        "utils",
    ]

    seed = "; ".join(
        [
            f'ABCLI_OBJECT_ROOT="{ABCLI_OBJECT_ROOT}"',
            f'BLUE_GEO_VERSION="{VERSION}"',
        ]
        + [
            'exec(Path(f\'{os.getenv("HOME")}/git/blue-geo/blue_geo/QGIS/console/'
            + module_name
            + ".py').read_text())"
            for module_name in list_of_modules
        ]
    )

    return seed
