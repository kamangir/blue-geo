from typing import Tuple
import requests
import json

from blueness import module

from blue_geo import NAME
from blue_geo.env import SKYFOX_ACCESS_TOKEN_URL, SKYFOX_CLIENT_ID, SKYFOX_CLIENT_SECRET
from blue_geo.catalog.generic.stac.classes import STACCatalog
from blue_geo.logger import logger

NAME = module.name(__file__, NAME)


class SkyFoxCatalog(STACCatalog):
    name = "skyfox"

    url = {
        "account": "https://console.earthdaily.com/account",
        "doc": "https://earthdaily.github.io/EDA-Documentation/",
        "platform": "https://console.earthdaily.com/platform",
        "signin": "https://console.earthdaily.com/mosaics/signin",
    }

    @staticmethod
    # https://earthdaily.github.io/EDA-Documentation/API/APIUsage/Python/#getting-the-authentication-token-for-pystac-client
    def get_new_token() -> Tuple[bool, str]:
        token_req_payload = {"grant_type": "client_credentials"}
        response = requests.post(
            SKYFOX_ACCESS_TOKEN_URL,
            data=token_req_payload,
            verify=False,
            allow_redirects=False,
            auth=(SKYFOX_CLIENT_ID, SKYFOX_CLIENT_SECRET),
        )

        # https://chat.openai.com/c/6deb94d0-826a-48de-b5ef-f7d8da416c82
        # response.raise_for_status()
        if response.status_code // 100 != 2:
            logger.error(f"SkyFoxCatalog.get_new_token() failed: {response}")
            return False, ""

        tokens = json.loads(response.text)

        return True, tokens["access_token"]
