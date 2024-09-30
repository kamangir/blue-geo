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

    def urls_as_str(self) -> List[str]:
        return sorted(
            [
                " - [{}]({})".format(
                    title.replace("-", " "),
                    url,
                )
                for title, url in self.url.items()
            ]
        )


class VoidCatalog(GenericCatalog):
    name = "void"
