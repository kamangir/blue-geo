from typing import Dict, List
from abcli.file.load import load_yaml


class Target:
    def __init__(self, filename: str = ""):
        self.items: List[Dict[str, Dict]] = []

        if filename:
            assert self.load(filename)

    def load(self, filename: str) -> bool:
        success, self.items = load_yaml(filename, civilized=True)
        return success
