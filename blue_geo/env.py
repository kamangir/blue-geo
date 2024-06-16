import os
from abcli.env import load_env, load_config

load_env(__name__)
load_config(__name__)


BLUE_GEO_CONFIG = os.getenv("BLUE_GEO_CONFIG", "")
