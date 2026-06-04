import json


def get_login_data():

    with open("test_data/login_data.json") as file:
        return json.load(file)