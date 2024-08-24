from datetime import datetime
from typing import Dict, List
from blue_options.options import Options
from abcli.file.load import load_yaml


class Target:
    def __init__(
        self,
        name: str = "",
        lat: float = 0,
        lon: float = 0,
        datetime: str = "",
    ) -> None:
        self.name: str = name

        self.lat = lat
        self.lon = lon

        self.datetime = datetime

    def default(self):
        self.name = "elkhema"
        self.datetime = "2022-08-06/"
        self.lat = 49.281209
        self.lon = -123.130760

    def __repr__(self) -> str:
        return "{}[{}]: @(lat={},lon={}) datetime".format(
            self.__class__.__name__,
            self.name,
            self.lat,
            self.lon,
            self.datetime,
        )


class TargetList:
    def __init__(self, filename: str = "") -> None:
        self.targets: Dict[str, Target] = {}

        if filename:
            self.load(filename)

    def get(self, description: str) -> Target:
        options = Options(description)

        if "name" in options:
            return self.targets.get(options["name"], Target())

        return Target(
            name=options.get("name", ""),
            lat=options.get("lat", 0),
            lon=options.get("lon", 0),
            datetime=options.get("datetime", ""),
        )

    def load(self, filename: str) -> bool:
        self.targets = {}

        success, targets = load_yaml(filename, civilized=True)

        for target_name, target_info in targets.items():
            self.targets[target_name] = Target(
                name=target_name,
                lat=target_info["lat"],
                lon=target_info["lon"],
                datetime=target_info["datetime"],
            )

        return success
