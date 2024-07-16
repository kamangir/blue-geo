import os
from abcli.env import load_env, load_config

load_env(__name__)
load_config(__name__)


UKRAINE_TIMEMAP_TEMPLATE = os.getenv("UKRAINE_TIMEMAP_TEMPLATE", "")

FIRMS_MAP_KEY = os.getenv("FIRMS_MAP_KEY", "")
