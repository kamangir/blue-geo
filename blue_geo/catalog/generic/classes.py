from typing import List, Dict


class GenericCatalog:
    name: str = "generic"

    url: Dict[str, str] = {
        "keyword": "url",
    }

    def __init__(self):
        pass

    def get_list_of_collections(self) -> List[str]:
        return []


class VoidCatalog(GenericCatalog):
    name = "void"
