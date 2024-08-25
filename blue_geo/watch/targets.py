import copy
from typing import Dict, List
from blue_options.options import Options
from abcli.file.load import load_yaml


class Target:
    def __init__(
        self,
        name: str = "",
        catalog: str = "",
        collection: str = "",
        args: Dict[str, str] = {},
    ) -> None:
        self.name: str = name

        self.catalog = catalog
        self.collection = collection

        self.args = copy.deepcopy(args)

    def __repr__(self) -> str:
        return "{}[{}]: {}/{}: {}".format(
            self.__class__.__name__,
            self.name,
            self.catalog,
            self.collection,
            self.args_as_str(" | "),
        )

    def args_as_str(self, delim: str = " ") -> str:
        return delim.join(
            [f"--{argument} {value}" for argument, value in self.args.items()]
        )


class TargetList:
    def __init__(self, filename: str = "") -> None:
        self.targets: Dict[str, Target] = {}

        if filename:
            self.load(filename)

    def load(self, filename: str) -> bool:
        self.targets = {}

        success, targets = load_yaml(filename, civilized=True)

        for target_name, target_info in targets.items():
            self.targets[target_name] = Target(
                name=target_name,
                catalog=target_info["catalog"],
                collection=target_info["collection"],
                args=target_info["args"],
            )

        return success
