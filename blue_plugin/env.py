import os
from abcli.env import load_env, load_config

load_env(__name__)
load_config(__name__)


BLUE_PLUGIN_SECRET = os.getenv(
    "BLUE_PLUGIN_SECRET",
    "",
)

BLUE_PLUGIN_CONFIG = os.getenv(
    "BLUE_PLUGIN_CONFIG",
    "",
)
