import json


def load_config(env="dev"):

    with open(f"config/{env}.json") as file:
        return json.load(file)