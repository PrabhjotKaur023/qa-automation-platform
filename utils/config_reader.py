import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def get_app_url():
    return config["app"]["base_url"]

def get_username():
    return config["credentials"]["username"]

def get_password():
    return config["credentials"]["password"]

def get_driver_path():
    return config["driver"]["chromedriver_path"]