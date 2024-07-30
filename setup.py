from blue_geo import NAME, VERSION, DESCRIPTION, REPO_NAME
from blueness.pypi import setup


setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.catalog",
        f"{NAME}.catalog.firms",
        f"{NAME}.catalog.firms.area",
        f"{NAME}.catalog.generic",
        f"{NAME}.datacube",
        f"{NAME}.QGIS",
        f"{NAME}.ukraine_timemap",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            ".abcli/**/*.sh",
            "**/README.md",
        ],
    },
)
