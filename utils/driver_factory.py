import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():

    options = Options()

    if os.getenv("CI"):

        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    else:

        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    return driver