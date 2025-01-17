import yaml


def Q_load_yaml(filename: str):
    with open(filename, "r") as file:
        return yaml.safe_load(file)
