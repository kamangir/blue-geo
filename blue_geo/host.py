from typing import List

from blueflow import fullname as blueflow_fullname
from abcli.host import signature as abcli_signature

from blue_geo import fullname


def signature() -> List[str]:
    return [
        fullname(),
        blueflow_fullname(),
    ] + abcli_signature()
