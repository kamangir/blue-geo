from typing import List

from notebooks_and_scripts import fullname as notebooks_ands_scripts_fullname
from abcli.host import signature as abcli_signature

from blue_geo import fullname


def signature() -> List[str]:
    return [
        fullname(),
        notebooks_ands_scripts_fullname(),
    ] + abcli_signature()
