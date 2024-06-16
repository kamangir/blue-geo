from blue_plugin import NAME, VERSION, DESCRIPTION, ICON
from blue_plugin.logger import logger
from blueness.argparse.generic import main

success, message = main(__file__, NAME, VERSION, DESCRIPTION, ICON)
if not success:
    logger.error(message)
