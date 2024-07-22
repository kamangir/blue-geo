from blue_geo import NAME, VERSION, DESCRIPTION, ICON
from blue_geo.logger import logger
from blue_geo import README
from blueness.argparse.generic import main

success, message = main(
    __file__,
    NAME,
    VERSION,
    DESCRIPTION,
    ICON,
    {
        "build_README": lambda _: README.build(),
    },
)
if not success:
    logger.error(message)
